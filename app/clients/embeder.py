from langchain_community.embeddings import SentenceTransformerEmbeddings

class Embeder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embedder = SentenceTransformerEmbeddings(model_name=model_name)

    def embed(self, text: str):
        return self.embedder.embed_query(text)
