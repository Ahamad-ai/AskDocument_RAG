# Ask Your Document RAG

A full-stack application for Question Answering (QnA) over your own PDF documents using Retrieval-Augmented Generation (RAG) with FastAPI, Streamlit, LangChain, OpenAI, and Groq LLMs. Upload PDFs, embed them into a vector database, and ask questions to get context-aware answers with relevant document snippets.

---

## Features
- **PDF Upload & Embedding:** Upload multiple PDFs and embed their content into a FAISS vector store.
- **RAG QnA:** Ask questions and get answers grounded in your uploaded documents using LLMs (Groq, OpenAI).
- **Web UI:** Modern frontend with file upload, question input, and answer/context display.
- **API & Streamlit:** Use either the FastAPI backend or the Streamlit app for interaction.
- **Dockerized:** Easy deployment with Docker.

---

## Tech Stack
- **Backend:** FastAPI, LangChain, FAISS, OpenAI, Groq
- **Frontend:** HTML/CSS/JS, Jinja2, Streamlit
- **Vector DB:** FAISS
- **PDF Parsing:** PyPDFLoader

---

## Getting Started

### 1. Clone the Repository
```bash
git clone <repo-url>
cd 3.RAG_DocumentQnA
```

### 2. Install Dependencies
It is recommended to use a virtual environment.
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory with the following:
```
GROQ_API_KEY=your_groq_api_key
OPEN_API_KEY=your_openai_api_key
```

### 4. Run with FastAPI
```bash
uvicorn app.main:app --reload
```
Visit [http://localhost:8000](http://localhost:8000)

### 5. Run with Streamlit
```bash
streamlit run streamlit_app.py
```

### 6. Docker (Optional)
```bash
docker build -t ask-document-rag .
docker run -p 8888:8888 ask-document-rag
```

---

## Usage
- **Upload PDFs:** Use the web UI to upload one or more PDF files.
- **Embed Documents:** Click the button to embed and index your documents.
- **Ask Questions:** Enter your question and get an answer with relevant context from your documents.

---

## Project Structure
```
├── app/
│   ├── main.py            # FastAPI app
│   ├── config.py          # Loads API keys from .env
│   ├── services/
│   │   ├── embeddings.py  # Embedding logic
│   │   └── retrieval.py   # Retrieval and QnA logic
│   ├── utils/
│   │   └── pdf_loader.py  # PDF loading utility
│   └── api/
│       └── routes.py      # (Optional) API routes
├── frontend/
│   ├── templates/index.html
│   └── static/            # CSS, JS, images
├── streamlit_app.py       # Streamlit interface
├── requirements.txt
├── Dockerfile
├── setup.py
└── ...
```

---

## Key Files
- `app/main.py`: FastAPI backend for file upload, embedding, and QnA endpoints.
- `streamlit_app.py`: Streamlit app for interactive QnA.
- `app/services/embeddings.py`: Handles document embedding and vector store creation.
- `app/services/retrieval.py`: Handles question answering using RAG.
- `frontend/templates/index.html`: Main web UI.

---

## License
This project is for personal hands-on practice and educational purposes only. Not intended for commercial use.

---

## Acknowledgements
- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://openai.com/)
- [Groq](https://groq.com/)
- [FAISS](https://github.com/facebookresearch/faiss)

---

## Author
- ahamad (<ahamadkv17@gmail.com>)
