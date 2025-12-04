from fastapi import FastAPI
from app.doctments import load_ducument

app = FastAPI(title="LLM/RAG API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/documents")
def documents():
    return {"status": load_ducument()}