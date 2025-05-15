from pydantic_settings import BaseSettings
import yaml
import os

class Settings(BaseSettings):
    app_name: str = "fastCursor API"
    debug: bool = True
    google_api_key: str
    prompt_version: str = "1.0"

    # LLM parameters (will be set dynamically)
    model_name: str = ""
    system: str = ""
    temperature: float = 0.7
    docs: str = ""
    max_tokens: int = 1024
    top_p: float = 0.95
    top_k: int = 40

    # Text split parameters
    chunk_size: int = 500
    chunk_overlap: int = 50

    pdf_url: str = ""

    class Config:
        env_file = ".env"

    def __init__(self, **values):
        super().__init__(**values)
        # Load prompts.yml
        with open("config/prompts.yml", "r") as f:
            config = yaml.safe_load(f)
        # Find the prompt config matching the version
        prompt = next(
            (p for p in config["prompts"] if str(p["version"]) == str(self.prompt_version)),
            None
        )
        if prompt:
            self.model_name = prompt.get("model_name", self.model_name)
            self.system = prompt.get("system", self.system)
            self.temperature = prompt.get("temperature", self.temperature)
            self.docs = prompt.get("docs", self.docs)
            self.max_tokens = prompt.get("max_tokens", self.max_tokens)
            self.top_p = prompt.get("top_p", self.top_p)
            self.top_k = prompt.get("top_k", self.top_k)
        else:
            raise ValueError(f"No prompt found for version {self.prompt_version}")

        # Update text split parameters
        self.chunk_size = int(os.getenv("CHUNK_SIZE", self.chunk_size))
        self.chunk_overlap = int(os.getenv("CHUNK_OVERLAP", self.chunk_overlap))

        self.pdf_url = os.getenv("PDF_URL", self.pdf_url)

settings = Settings()
