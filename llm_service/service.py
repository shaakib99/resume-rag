from llm_service.llm_abc import LLMABC
class LLMService:
    def __init__(self, llm: LLMABC):
        self.llm = llm
    
    async def ask(self, 
                  human_prompt: HumanMessage, 
                  system_prompt: SystemMessage = SystemMessage(content="You are a helpful assistant."),  
                  tools: list[BaseTool] = [], 
                  middlewares: list[AgentMiddleware] = [], 
                  context: BaseContext | None = None,
                  name: str = 'ResumeAgent'
                  ):
        return await self.llm.ask(
            human_prompt=human_prompt, 
            system_prompt=system_prompt, 
            tools=tools, 
            middlewares=middlewares, 
            context=context, 
            name=name
        )