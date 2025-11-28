from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.cors import CORS_CONFIG
from src.book.routes import book_router

version = 'v1'
app = FastAPI(
    version= version,
    title= 'Bookly',
    description= 'A web api for book review service'
)

app.add_middleware(
    CORSMiddleware,
    **CORS_CONFIG
)
app.include_router(book_router, prefix=f'/api/{version}/books', tags=['books'])

