from pydantic import BaseModel

class BaseContext(BaseModel):
    context: str = ''

class BaseModelResponseFormat(BaseModel):
    response: str
