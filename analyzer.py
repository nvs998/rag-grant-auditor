import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from ingest import get_vector_store
from prompts import get_grant_audit_prompt

load_dotenv()

# Serverless supported model ID on the HF Router
# REPO_ID = "meta-llama/Llama-3.2-3B-Instruct"
REPO_ID = "Qwen/Qwen3-4B-Instruct-2507"
# REPO_ID = "Qwen/Qwen3-4B-Instruct"

def get_llm():
    """Initialize Hugging Face Inference API endpoint using Chat Router."""
    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not hf_token:
        raise ValueError("HUGGINGFACEHUB_API_TOKEN is missing in your .env file.")

    endpoint = HuggingFaceEndpoint(
        repo_id=REPO_ID,
        huggingfacehub_api_token=hf_token,
        temperature=0.2,
        max_new_tokens=1024,
    )
    return ChatHuggingFace(llm=endpoint)

def audit_pitch(pitch_text: str) -> str:
    """Core function to query ChromaDB, retrieve context, and run the Hugging Face LLM pipeline."""
    print("🔍 Searching ChromaDB for relevant grant criteria...")
    vector_store = get_vector_store()
    
    # Retrieve top 4 relevant context chunks matching the pitch content
    retrieved_docs = vector_store.similarity_search(pitch_text, k=4)
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    print("🧠 Querying Hugging Face LLM for readiness audit...")
    prompt = get_grant_audit_prompt()
    llm = get_llm()
    
    messages = prompt.invoke({
        "context": context,
        "pitch_text": pitch_text,
    })

    try:
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        print(f"⚠️ Inference Error: {e}")
        raise e  # Caught by app.py st.spinner wrapper to trigger fallback

if __name__ == "__main__":
    weak_pitch_file = "sample_pitch.txt"
    if os.path.exists(weak_pitch_file):
        with open(weak_pitch_file, "r") as f:
            sample_text = f.read()
            
        print("📄 Loaded sample weak pitch for testing...")
        report = audit_pitch(sample_text)
        print("\n" + "="*50 + "\nAUDIT OUTPUT:\n" + "="*50)
        print(report)
    else:
        print(f"File {weak_pitch_file} not found. Please create it to test.")