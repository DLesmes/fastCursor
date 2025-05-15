from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.clients.embeder import Embeder
from app.settings import settings

class Retriever:
    def __init__(self, persist_directory="chroma_db"):
        self.embeder = Embeder()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
        self.persist_directory = persist_directory
        self.vectorstore = Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embeder.embedder
        )

    def add_documents(self, documents: list):
        # Split and add documents to the vectorstore
        texts = []
        for doc in documents:
            texts.extend(self.text_splitter.split_text(doc))
        self.vectorstore.add_texts(texts)

    def retrieve(self, query: str, k=3):
        # Retrieve top-k relevant documents
        docs = self.vectorstore.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]
