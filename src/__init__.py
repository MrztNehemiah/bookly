from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import CORS_CONFIG
from src.book.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app:FastAPI):
    
    print(f'Server is starting...')
    await init_db()
    yield
    print(f'Server has been stopped!')
version = 'v1'
app = FastAPI(
    version= version,
    title= 'Bookly',
    description= 'A web api for book review service',
    lifespan= life_span
)

app.add_middleware(
    CORSMiddleware,
    **CORS_CONFIG
)
app.include_router(book_router, prefix=f'/api/{version}/books', tags=['books'])

