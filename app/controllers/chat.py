from fastapi import APIRouter, HTTPException, Query
from app.services.agent import Agent

router = APIRouter()

@router.post("/chat/message")
def chat_message(
    session_id: str = Query(..., description="Session ID"),
    message: str = Query(..., description="Message to send to the LLM")
):
    try:
        agent = Agent()
        response = agent.get_llm_response(session_id, message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))