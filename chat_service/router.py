from fastapi import APIRouter

chat_router = APIRouter(prefix='/q', tags=['chat'])

@chat_router.post()
async def create(data: dict):
    return {'message': 'success'}

@chat_router.get('{id}')
async def get_one(id: str):
    return {}

@chat_router.get()
async def get_all(query: dict):
    return []
