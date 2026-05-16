from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from chat_service.service import ChatService

chat_router = APIRouter(prefix='/q', tags=['chat'])

chat_service = ChatService()

@chat_router.post('')
async def create(data: dict):
    async def create_data(data: dict):
        async for chunk in chat_service.create(data):
            yield chunk
    
    return StreamingResponse(create_data(data), media_type='text/event-stream')

@chat_router.get('{id}')
async def get_one(id: str):
    return {}

@chat_router.get('')
async def get_all(query: dict):
    return []
