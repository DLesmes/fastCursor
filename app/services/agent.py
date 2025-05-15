from app.services.memory import memory
from app.clients.llm import LLM
from app.services.retriever import Retriever
from app.settings import settings

class Agent:
    def __init__(self):
        self.memory = memory
        self.llm = LLM()
        self.retriever = Retriever()

    def get_llm_response(self, session_id: str, message: str):
        # Retrieve conversation state (history)
        state = self.memory.get_state(session_id)

        # Retrieve relevant docs
        retrieved_docs = self.retriever.retrieve(message)
        state.retrieved_docs = retrieved_docs

        # Build context from history
        context = ""
        for turn in state.history:
            context += f"User: {turn['user']}\nAgent: {turn['agent']}\n"
        context += f"User: {message}\nAgent:"

        # Add retrieved docs using the docs prompt template from settings
        docs_prompt = settings.docs
        docs_context = "\n".join(retrieved_docs)
        full_prompt = f"{docs_prompt}\n\n{docs_context}\n\n{context}" if docs_context else context

        # Send the full context to the LLM
        response = self.llm.send_message(session_id, full_prompt)

        # Update memory with the new message and response
        self.memory.update_state(session_id, message, response)
        return response
