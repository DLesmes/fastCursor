import yaml
from langchain_google_genai import ChatGoogleGenerativeAI

class LLM:
    def __init__(self, config_path="config/prompts.yml"):
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        self.prompt_config = config["prompts"][0]
        self.model = ChatGoogleGenerativeAI(
            model=self.prompt_config["model_name"],
            temperature=self.prompt_config["temperature"],
            max_output_tokens=self.prompt_config["max_tokens"],
            top_p=self.prompt_config["top_p"],
            top_k=self.prompt_config["top_k"],
        )

    def send_message(self, session_id: str, message: str):
        # You can use session_id for context management if needed
        response = self.model.invoke(message)
        return response.content if hasattr(response, "content") else response
