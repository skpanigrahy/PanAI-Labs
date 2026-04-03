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


# global instance
doc_store = DocumentStore()