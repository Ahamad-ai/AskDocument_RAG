# embedding.py

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.utils.pdf_loader import load_documents_from_paths
from app.config import OPENAI_API_KEY

VECTOR_DIR = "vectorstore_index"
_documents = []
_vectorstore = None

def process_and_embed_documents(file_paths):
    global _vectorstore, _documents

    docs = load_documents_from_paths(file_paths)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    _documents = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    _vectorstore = FAISS.from_documents(_documents, embeddings)
    _vectorstore.save_local(VECTOR_DIR)

    print(f"✅ Embedded {len(_documents)} chunks across {len(file_paths)} PDFs.")

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        _vectorstore = FAISS.load_local(VECTOR_DIR, embeddings)
    return _vectorstore