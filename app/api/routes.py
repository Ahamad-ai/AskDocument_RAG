from fastapi import APIRouter, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import os
from typing import List

from app.services.embedding import process_and_embed_documents
from app.services.retrieval import query_documents

router = APIRouter()
templates = Jinja2Templates(directory="frontend/templates")

# Route to serve homepage
@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Route to handle file uploads
@router.post("/upload/")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    saved_files = []
    for file in files:
        file_path = os.path.join("uploads", file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        saved_files.append(file_path)

    try:
        process_and_embed_documents(saved_files)
        return JSONResponse(content={"message": "✅ Documents embedded successfully!"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


# Route to handle queries
@router.post("/query/")
async def ask_question(question: str = Form(...)):
    try:
        answer, contexts = query_documents(question)
        return JSONResponse(content={"answer": answer, "context": contexts})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)