import streamlit as st
import os
import time
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS

load_dotenv()

# Set API Keys
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPEN_API_KEY")

# Initialize LLM
llm = ChatGroq(groq_api_key=os.environ["GROQ_API_KEY"], model="gemma2-9b-it")

# Prompt Template
prompt = ChatPromptTemplate.from_template("""
Answer the question based on the provided context only.
Please provide the most accurate response based on the question.

<context>
{context}
<context>

Question: {input}
""")

# Streamlit App Title
st.title("📄 Ask Your Document")

# File Uploader
uploaded_files = st.file_uploader("Upload your PDF files", type=["pdf"], accept_multiple_files=True)

# Vector Embedding Logic
def create_vector_embeddings(files):
    docs = []
    for file in files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())
        loader = PyPDFLoader(file.name)
        docs.extend(loader.load())

    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(final_documents, embeddings)
    st.session_state.vectorstore = vectorstore
    st.session_state.documents = final_documents

# Embed Button
if uploaded_files and st.button("📌 Create Document Embeddings"):
    create_vector_embeddings(uploaded_files)
    st.success("✅ Vector DB is ready for querying!")

# Query Input
user_prompt = st.text_input("🔍 Enter your question")

# Search Logic
if user_prompt and "vectorstore" in st.session_state:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectorstore.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start_time = time.process_time()
    response = retrieval_chain.invoke({"input": user_prompt})
    elapsed = time.process_time() - start_time

    st.subheader("📘 Answer")
    st.write(response["answer"])
    st.caption(f"⏱️ Processed in {elapsed:.2f} seconds")

    with st.expander("🧠 Document Similarity Search"):
        for doc in response.get("context", []):
            st.markdown(doc.page_content)
            st.markdown("---")