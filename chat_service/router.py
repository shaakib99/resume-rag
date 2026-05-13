from fastapi import APIRouter
from chat_service.service import ChatService

chat_router = APIRouter(prefix='/q', tags=['chat'])

chat_service = ChatService()

@chat_router.post('')
async def create(data: dict):
    return await chat_service.create(data)

@chat_router.get('{id}')
async def get_one(id: str):
    return {}

@chat_router.get('')
async def get_all(query: dict):
    return []
