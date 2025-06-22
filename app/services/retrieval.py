# retrieval.py

import os
from app.services.embeddings import get_vectorstore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="gemma2-9b-it"
)

prompt = ChatPromptTemplate.from_template("""
Answer the question based on the provided context only.
Please provide the most accurate response based on the question.

<context>
{context}
<context>

Question: {input}
""")

def query_documents(question: str):
    vectorstore = get_vectorstore()
    if not vectorstore:
        raise ValueError("⚠️ Vectorstore is not available. Please upload and embed documents first.")

    retriever = vectorstore.as_retriever()
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    result = retrieval_chain.invoke({"input": question})
    answer = result.get("answer", "No answer found.")
    context = [doc.page_content for doc in result.get("context", [])]

    return answer, context