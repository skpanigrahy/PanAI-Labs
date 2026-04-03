from services.llm import call_llm
from rag.store import doc_store
from rag.retriever import retrieve

def run_rag_agent(messages):
    user_query = messages[-1]["content"]

    documents = doc_store.get_all()
    retrieved_chunks = retrieve(user_query, documents)

    context = "\n".join(retrieved_chunks)

    prompt = [
        {
            "role": "system",
            "content": "Answer the question using ONLY the provided context."
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {user_query}"
        }
    ]

    return call_llm(prompt)