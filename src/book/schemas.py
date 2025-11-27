from pydantic import BaseModel

#Validating the Books info types with pydantic BaseModel
class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    year: int
    isbn: str
    available: bool

class BookUpdate(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    isbn: str
    available: bool
