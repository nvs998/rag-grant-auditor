from ingest import get_vector_store

def test_query(query_text: str):
    print(f"\n🔍 Testing Query: '{query_text}'")
    vector_store = get_vector_store()
    
    # Retrieve top 2 most relevant chunks
    results = vector_store.similarity_search(query_text, k=2)
    
    print(f"Found {len(results)} matching chunks:\n" + "-"*40)
    for i, doc in enumerate(results, 1):
        print(f"Chunk {i}:\n{doc.page_content}\n" + "-"*40)

if __name__ == "__main__":
    # Test queries aligned with our grant mandates
    test_query("What are the budgeting and co-financing rules?")
    test_query("What team roles are required?")