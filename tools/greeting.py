from langchain.tools import tool

@tool("greet", return_direct=True)
def greet(name: str) -> str:
    """Greet a person by their name."""
    print(f"Greeting tool called with name: {name}")
    return f"Hello, How are you {name}!"