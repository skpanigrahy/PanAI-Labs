class DocumentStore:
    def __init__(self):
        self.docs = []

    def add_document(self, text: str):
        chunks = self.chunk_text(text)
        self.docs.extend(chunks)

    def chunk_text(self, text: str, size: int = 200):
        words = text.split()
        chunks = []

        for i in range(0, len(words), size):
            chunk = " ".join(words[i:i+size])
            chunks.append(chunk)

        return chunks

    def get_all(self):
        return self.docs

    def retrieve(query: str, documents: list, top_k: int = 3):
        query_words = set(query.lower().split())

        scored = []

        for doc in documents:
            doc_words = set(doc.lower().split())
            score = len(query_words & doc_words)
            scored.append((score, doc))

        scored.sort(reverse=True, key=lambda x: x[0])

        return [doc for score, doc in scored[:top_k]]

def retrieve(query: str, documents: list, top_k: int = 3):
        query_words = set(query.lower().split())

        scored = []

        for doc in documents:
            doc_words = set(doc.lower().split())
            score = len(query_words & doc_words)
            scored.append((score, doc))

        scored.sort(reverse=True, key=lambda x: x[0])

        return [doc for score, doc in scored[:top_k]]

# global instance
doc_store = DocumentStore()