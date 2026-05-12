from abc import ABC, abstractmethod
from langchain.messages import SystemMessage, HumanMessage, ToolCall
from langchain.tools import BaseTool
from langchain.agents.middleware import AgentMiddleware
from llm_service.models import BaseContext, BaseModelResponseFormat

class LLMABC(ABC):
    def __init__(self, model_name: str, tools: list[ToolCall]):
        pass
        
    @abstractmethod
    async def ask(self, human_prompt: HumanMessage, 
                  system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant."),  
                  tools: list[BaseTool] = [], 
                  middlewares: list[AgentMiddleware] = [], 
                  context: BaseContext | None = None,
                  name: str = 'ResumeAgent') -> BaseModelResponseFormat:
        pass