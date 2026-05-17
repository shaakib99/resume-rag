from pydantic import BaseModel

class BaseContext(BaseModel):
    context: str = ''
    user_email: str = None
    thread_id: str = None


class BaseModelResponseFormat(BaseModel):
    response: str
