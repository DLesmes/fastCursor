from langchain_google_genai import ChatGoogleGenerativeAI
from app.settings import settings

class LLM:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model=settings.model_name,
            temperature=settings.temperature,
            max_output_tokens=settings.max_tokens,
            top_p=settings.top_p,
            top_k=settings.top_k,
            google_api_key=settings.google_api_key
        )

    def send_message(self, session_id: str, message: str):
        # You can use session_id for context management if needed
        response = self.model.invoke(message)
        return response.content if hasattr(response, "content") else response
