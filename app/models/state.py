from pydantic import BaseModel

class State(BaseModel):
    session_id: str
    history: list  # You can refine this structure as needed
    retrieved_docs: list = []
