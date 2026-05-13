from llm_service.llm_abc import LLMABC
from langchain.tools import BaseTool
from langchain.messages import HumanMessage, SystemMessage
from llm_service.models import BaseContext
from langchain.agents.middleware import AgentMiddleware
from llm_service.openrouter_llm import OpenRouterLLM
import os

class LLMService:
    def __init__(self, llm: LLMABC = None):
        self.llm = llm or OpenRouterLLM(model_name=os.getenv("OPENROUTER_MODEL_NAME"))
    
    async def ask(self, 
                  human_prompt: HumanMessage, 
                  system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant."),  
                  tools: list[BaseTool] = [], 
                  middlewares: list[AgentMiddleware] = [], 
                  context: BaseContext | None = None,
                  name: str = 'ResumeAgent'
                  ):
        result = await self.llm.ask(
            human_prompt=human_prompt, 
            system_prompt=system_prompt, 
            tools=tools,
            middlewares=middlewares, 
            context=context, 
            name=name
        )
        return result