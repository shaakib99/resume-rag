from llm_service.llm_abc import LLMABC
from langchain.agents import create_agent
from langchain.tools import BaseTool
from langchain.chat_models import BaseChatModel, init_chat_model
from langchain.messages import HumanMessage, SystemMessage
from llm_service.models import BaseContext, BaseModelResponseFormat
from langchain.agents.middleware import AgentMiddleware
from langchain.agents.structured_output import ProviderStrategy

class OpenRouterLLM(LLMABC):
    def __init__(self, model_name):
        self.model_name = model_name
        self.model: BaseChatModel = init_chat_model(model_name)
    
    async def ask(self, 
                  human_prompt: HumanMessage, 
                  system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant."),  
                  tools: list[BaseTool] = [], 
                  middlewares: list[AgentMiddleware] = [], 
                  context: BaseContext | None = None,
                  name: str = 'OpenRouterAgent'
                  ):
        self.agent = create_agent(
            model = self.model, 
            tools=tools, 
            system_prompt=system_prompt, 
            middlewares=middlewares, 
            name=name, 
            context_schema=BaseContext,
            response_format=ProviderStrategy(BaseModelResponseFormat)
            )
        result = self.agent.invoke({'messages': {'role': 'user', 'content': human_prompt }}, context=context)
        return result