from langchain.agents.middleware import wrap_model_call, wrap_tool_call, ModelRequest, ModelResponse
from typing import Callable

@wrap_model_call
async def dynamic_model_selection(request: ModelRequest, handler):
    # Here you can implement logic to select a model based on the request
    print(f"Model Request: {request}")
    response = await handler(request)
    print(f"Model Response: {response}")
    return response

@wrap_model_call
async def get_user_information_wrapper(request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse:
    user_email = request.runtime.context.user_email
    print(f"Middleware: Checking for user_email in context: {user_email}")
    if not user_email:
        existing_tools = [t for t in request.tools if t.name != "get_user_information"]
        request = request.override(tools=[*existing_tools])
    return await handler(request)
    # return ToolMessage(content=response)

@wrap_tool_call
async def tool_call_wrapper(request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse:
    # print(f"Middleware: Tool call wrapper invoked for tool: {request.tool.name}")
    response = await handler(request)
    print(f"Middleware: Tool call wrapper received response: {response}")
    return response