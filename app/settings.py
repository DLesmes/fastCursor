from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "fastCursor API"
    debug: bool = True
    google_api_key: str = "GOOGLE_API_KEY"

    class Config:
        env_file = ".env"

settings = Settings()
