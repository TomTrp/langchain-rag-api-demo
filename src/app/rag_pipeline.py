from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_huggingface import HuggingFaceEmbeddings
from config import HUGGINGFACEHUB_API_TOKEN

def split_docs_to_chunk(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    docs_split = splitter.split_documents(docs)
    return docs_split

def get_chat_model() -> ChatHuggingFace:
    llm = HuggingFaceEndpoint(
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
        repo_id="deepseek-ai/DeepSeek-R1-0528",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
        provider="auto",  # let Hugging Face choose the best provider for you
    )
    chat_model = ChatHuggingFace(llm=llm)
    return chat_model

def embeddings():
    hf = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": False},
    )
    return hf
