

from langchain.messages import HumanMessage
from llm_service.service import LLMService
from tools.greeting import greet
from tools.database import get_user_information, create_user_information


class ChatService:
    def __init__(self, llm_service = None):
        self.llm_service = llm_service or LLMService()
    
    async def create(self, data: dict):
        if self.llm_service is None: raise ValueError("LLM Service is not set.")
        prompt = data.get('prompt') or 'Nothing to say.'
        print(f"Received prompt: {prompt}")
        human_message = HumanMessage(prompt)
        response = await self.llm_service.ask(human_message, tools=[greet, create_user_information, get_user_information])
        return response