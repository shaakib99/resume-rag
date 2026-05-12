

from langchain.messages import HumanMessage
from llm_service.service import LLMService


class ChatService:
    def __init__(self, llm_service = None):
        self.llm_service = llm_service or LLMService()
    
    async def create(self, prompt: str):
        if self.llm_service is None: raise ValueError("LLM Service is not set.")
        human_message = HumanMessage('Hello, how are you?')
        response = await self.llm_service.ask(human_message)
        return response