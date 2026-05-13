from llm_service.llm_abc import LLMABC
from langchain.agents import create_agent
from langchain.tools import BaseTool
from langchain.chat_models import BaseChatModel, init_chat_model
from langchain.messages import HumanMessage, SystemMessage
from llm_service.models import BaseContext, BaseModelResponseFormat
from langchain.agents.middleware import AgentMiddleware
from langchain.agents.structured_output import ProviderStrategy
from langchain_openrouter import ChatOpenRouter
import os

class OpenRouterLLM(LLMABC):
    def __init__(self, model_name: str):
        self.model: BaseChatModel = ChatOpenRouter(model=model_name, api_key=os.getenv("OPENROUTER_API_KEY"))
    
    async def ask(self, 
                  human_prompt: HumanMessage, 
                  system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant. You will respond to the user's query in a helpful and concise manner."),  
                  tools: list[BaseTool] = [], 
                  middlewares: list[AgentMiddleware] = [], 
                  context: BaseContext | None = None,
                  name: str = 'OpenRouterAgent'
                  ):
        agent = create_agent(
            model = self.model, 
            tools=tools, 
            system_prompt=system_prompt, 
            middleware=middlewares, 
            name=name, 
            context_schema=BaseContext
            # response_format=ProviderStrategy(BaseModelResponseFormat)
            )
        response = await agent.ainvoke({'messages': [system_prompt, human_prompt]}, context=context)
        return response['messages'][-1].content