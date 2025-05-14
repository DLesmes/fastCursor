from fastapi import FastAPI
from app.controllers import chat
import uvicorn

app = FastAPI(title="fastCursor API")
app.include_router(chat.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to fastCursor API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
