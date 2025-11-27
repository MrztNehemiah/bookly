from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
    available = bool

@app.get('/books')
def view_books():
    return bookshelf

@app.post('/books')
def create_book():
    pass

@app.get('/book/{book_id}')
def view_a_book(book_id):
    pass

@app.patch('/book/{book_id}')
def update_book_shelf(book_id):
    pass

@app.delete('/book/{book_id}')
def delete_book(book_id):
    pass