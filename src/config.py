import os
from dotenv import load_dotenv

load_dotenv()

DOCS_PATH = os.environ.get("DOCS_PATH", "./docs")
HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
CHROMA_HOST = os.environ.get("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.environ.get("CHROMA_PORT", "8000"))