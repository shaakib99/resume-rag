from abc import ABC, abstractmethod
from langchain.messages import SystemMessage, HumanMessage, ToolCall

class LLMABC(ABC):
    def __init__(self, model_name: str, tools: list[ToolCall]):
        pass
        
    @abstractmethod
    async def ask(self, human_message: HumanMessage, system_message: SystemMessage):
        pass