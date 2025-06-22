import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents_from_paths(file_paths):
    """
    Loads and returns all documents from the list of PDF file paths.
    """
    documents = []
    for path in file_paths:
        if os.path.exists(path) and path.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
        else:
            raise FileNotFoundError(f"File not found or unsupported format: {path}")
    return documents