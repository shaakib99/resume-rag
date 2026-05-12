from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from chat_service.router import chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield

app = FastAPI(lifespan=lifespan)

routers: list[APIRouter] = [chat_router]
for router in routers: app.include_router(router)