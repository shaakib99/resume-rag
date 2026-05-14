from langchain.tools import tool

users = [{
    "name": "Wahid Sakib",
    "email": "wahidsakib@email.com",
    "age": 30,
    "location": "Dhaka, Bangladesh"
}]
@tool("get_user_information")
async  def get_user_information(user_email: str) -> dict:
    """Fetch user information based on user email."""
    return get_user(user_email)

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