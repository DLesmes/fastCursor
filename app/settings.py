

class Settings():
    app_name: str = "fastCursor API"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
