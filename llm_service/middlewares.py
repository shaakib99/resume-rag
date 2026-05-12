from langchain.agents.middleware import wrap_model_call, wrap_tool_call, ModelRequest, ModelResponse, ToolCallRequest, ToolCallResponse

@wrap_model_call
async def dynamic_model_selection(request: ModelRequest, handler):
    # Here you can implement logic to select a model based on the request
    print(f"Model Request: {request}")
    response = await handler(request)
    print(f"Model Response: {response}")
    return response