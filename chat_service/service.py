

from langchain.messages import HumanMessage
from llm_service.service import LLMService
from tools.greeting import greet
from tools.database import get_user_information, create_user_information, get_user
from llm_service.models import BaseContext

class ChatService:
    def __init__(self, llm_service = None):
        self.llm_service = llm_service or LLMService()
    
    async def create(self, data: dict):
        if self.llm_service is None: raise ValueError("LLM Service is not set.")
        prompt = data.get('prompt') or 'Nothing to say.'
        human_message = HumanMessage(prompt)
        user_data = await get_user(user_email="wsakib87@gmail.com")
        context = BaseContext(context=f'''
        This is the user information in database. Use this information to answer the user's query if needed. Do not use this information if it is not relevant to the user's query.
        Context: {user_data}''')
        response = await self.llm_service.ask(human_message, tools=[greet, create_user_information, get_user_information], context=context)
        return response