from typing import AsyncGenerator

from llm_service.llm_abc import LLMABC
from langchain.agents import create_agent
from langchain.tools import BaseTool
from langchain.chat_models import BaseChatModel, init_chat_model
from langchain.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
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
                  ) -> AsyncGenerator[str, None, None]:
        if context.context: system_prompt = SystemMessage(content=f"{system_prompt.content}\n\n{context.context}")
        
        agent = create_agent(
            model = self.model, 
            tools=tools, 
            system_prompt=system_prompt, 
            middleware=middlewares,
            name=name, 
            context_schema=BaseContext,
            # response_format=ProviderStrategy(BaseModelResponseFormat)
            )
        async for chunk in agent.astream({'messages': [system_prompt, human_prompt]}, context=context, stream_mode="messages", version="v2"):
            chunk_message = chunk['data'][0]  # ✅ dict → data → first element
            if isinstance(chunk_message, AIMessage) and chunk_message.content:
                # print(f"Chunk content: {chunk_message.content}")  # ✅ Log the content of the chunk
                yield chunk_message.content
            # ✅ Stream tool call — so no silence gap
            elif hasattr(chunk_message, 'tool_call_chunks') and chunk_message.tool_call_chunks:
                tool_name = chunk_message.tool_call_chunks[0].get('name')
                if tool_name:
                    yield f"\n[Calling tool: {tool_name}...]\n"
            
            # ✅ Stream tool result
            elif isinstance(chunk_message, ToolMessage):
                yield f"\n{chunk_message.content}\n"