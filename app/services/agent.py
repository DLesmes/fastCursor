from app.clients.llm import LLM

class Agent:
    def __init__(self):
        self.llm_client = LLM()

    def get_llm_response(self, session_id: str, message: str):
        return self.llm_client.send_message(session_id, message)
