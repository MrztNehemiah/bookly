from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


bookshelf = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "genre": "Programming",
        "year": 2008,
        "isbn": "978-0132350884",
        "available": True
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt, David Thomas",
        "genre": "Programming",
        "year": 1999,
        "isbn": "978-0201616224",
        "available": False
    },
    {
        "id": 3,
        "title": "Deep Learning with Python",
        "author": "François Chollet",
        "genre": "Machine Learning",
        "year": 2017,
        "isbn": "978-1617294433",
        "available": True
    },
    {
        "id": 4,
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Self-help",
        "year": 2018,
        "isbn": "978-0735211292",
        "available": True
    },
    {
        "id": 5,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "genre": "Programming",
        "year": 2015,
        "isbn": "978-1593276034",
        "available": False
    }
]

#Validating the Books info types with pydantic BaseModel
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    year: int
    isbn: str
    available: bool

@app.get('/books', response_model= list[Book])
async def view_books():
    return bookshelf

@app.post('/books')
async def create_book(book_data:Book, status_code=status.HTTP_201_CREATED) -> dict:
    #Generate a dictionary representation of the model
    new_book = book_data.model_dump()
    bookshelf.append(new_book)
    return new_book

@app.get('/books/{book_id}')
async def view_a_book(book_id):
    book_id = int(book_id)
    for book in bookshelf:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not Found')

@app.patch('/book/{book_id}')
async def update_book_shelf(book_id):
    pass

@app.delete('/book/{book_id}')
async def delete_book(book_id):
    pass