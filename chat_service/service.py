from collections.abc import AsyncGenerator
from langchain.messages import HumanMessage
from llm_service.service import LLMService
from tools.greeting import greet
from tools.database import get_user_information, create_user_information, get_user, get_user_information_wrapper, tool_call_wrapper
from llm_service.models import BaseContext

class ChatService:
    def __init__(self, llm_service = None):
        self.llm_service = llm_service or LLMService()
    
    async def create(self, data: dict) -> AsyncGenerator[str, None, None]:
        if self.llm_service is None: raise ValueError("LLM Service is not set.")
        prompt = data.get('prompt') or 'Nothing to say.'
        human_message = HumanMessage(prompt)
        user_data = await get_user(user_email="wahidsakib@email.com")
        context = BaseContext(context=f'''
        This is the user information in database. Use this information to answer the user's query if needed. Do not use this information if it is not relevant to the user's query.
        Context: user email: {user_data['email']}''', user_email="wahidsakib@email.com")

        async for chunk in self.llm_service.ask(
            human_message, 
            tools=[greet, get_user_information, create_user_information], 
            context=context, 
            middlewares=[get_user_information_wrapper, tool_call_wrapper]
        ):
            yield chunk