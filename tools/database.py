from langchain.tools import tool
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse, wrap_tool_call
from typing import Callable
from langchain.messages import ToolMessage

users = [{
    "name": "Wahid Sakib",
    "email": "wahidsakib@email.com",
    "age": 30,
    "location": "Dhaka, Bangladesh"
}]

@tool("get_user_information")
async  def get_user_information(user_email: str) -> dict:
    """Get the current user's complete information including name, email, age, and location. 
    Use this tool when you need to access user details like age, location, or name.
    The user's email is already known from the context, so no parameters are needed."""
    # Get email from context - you need to pass this differently
    print(f"Tool: get_user_information called with user_email: {user_email}")
    return await get_user(user_email)

@tool("create_user_information")
async  def create_user_information(name: str, email: str, age: int, location: str) -> dict:
    """Create user information."""
    # Simulate creating user information in a database or external service
    user_info = {
        "name": name,
        "email": email,
        "age": age,
        "location": location
    }
    users.append(user_info)
    return user_info

async def get_user(user_email: str) -> dict:
    """Fetch user information based on user email."""
    print(f"Fetching information for user_email: {user_email}")
    # Simulate fetching user information from a database or external service
    user_info = next((user for user in users if user['email'] == user_email), None)
    return user_info

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