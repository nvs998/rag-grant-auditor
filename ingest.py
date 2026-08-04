import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

DB_DIR = "./chroma_db"
GUIDELINES_FILE = "grant_guidelines.txt"

# Free, fast, local embedding model
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

def build_vector_store():
    if not os.path.exists(GUIDELINES_FILE):
        raise FileNotFoundError(f"{GUIDELINES_FILE} not found. Please create it first.")

    print("📄 Loading grant guidelines...")
    loader = TextLoader(GUIDELINES_FILE)
    documents = loader.load()

    print("✂️ Chunking documents...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} text chunks.")

    print(f"🧠 Generating local embeddings using '{EMBEDDING_MODEL_NAME}' and saving to ChromaDB...")
    embeddings = get_embeddings()
    
    # Reset existing DB if re-building with new embedding dimension
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    
    print("✅ Vector store successfully created with HuggingFace embeddings at ./chroma_db")
    return vector_store

def get_vector_store():
    """Helper function to load the persisted vector store."""
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )

if __name__ == "__main__":
    build_vector_store()