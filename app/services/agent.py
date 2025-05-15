from app.services.memory import memory
from app.clients.llm import LLM

class Agent:
    def __init__(self):
        self.memory = memory
        self.llm = LLM()

    def get_llm_response(self, session_id: str, message: str):
        # Retrieve conversation state (history)
        state = self.memory.get_state(session_id)

        # Build context from history
        context = ""
        for turn in state.history[-10:]:
            context += f"User: {turn['user']}\nAgent: {turn['agent']}\n"
        context += f"User: {message}\nAgent:"

        # Send the full context to the LLM
        response = self.llm.send_message(session_id, context)

        # Update memory with the new message and response
        self.memory.update_state(session_id, message, response)
        return response
