import os
import requests
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.clients.embeder import Embeder
from app.settings import settings
from pypdf import PdfReader

class Retriever:
    def __init__(self, persist_directory="chroma_db"):
        self.embeder = Embeder()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
        self.persist_directory = persist_directory

        # Check if the vectorstore already exists (ChromaDB stores an index in the directory)
        if not os.path.exists(self.persist_directory) or not os.listdir(self.persist_directory):
            self.vectorstore = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeder.embedder
            )
            self._build_index_from_pdf(settings.pdf_url)
        else:
            self.vectorstore = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeder.embedder
            )

    def _build_index_from_pdf(self, pdf_url):
        pdf_path = "temp.pdf"
        # Download PDF if not already present
        if not os.path.exists(pdf_path):
            print(f"Downloading PDF from {pdf_url}...")
            response = requests.get(pdf_url)
            with open(pdf_path, "wb") as f:
                f.write(response.content)
        # Extract text from PDF
        reader = PdfReader(pdf_path)
        full_text = ""
        for page in reader.pages:
            full_text += page.extract_text() or ""
        # Split and add to vectorstore
        texts = self.text_splitter.split_text(full_text)
        if texts:
            self.vectorstore.add_texts(texts)
            print(f"Indexed {len(texts)} chunks from PDF.")

    def retrieve(self, query: str, k=3):
        docs = self.vectorstore.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]
