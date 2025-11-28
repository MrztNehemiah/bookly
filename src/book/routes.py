from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.book.book_data import bookshelf
from src.book.schemas import Book, BookUpdate

book_router = APIRouter()

@book_router.get('/', response_model= list[Book])
async def view_books():
    return bookshelf

@book_router.post('/')
async def create_book(book_data:Book, status_code=status.HTTP_201_CREATED) -> dict:
    #Generate a dictionary representation of the model
    new_book = book_data.model_dump()
    bookshelf.append(new_book)
    return new_book

@book_router.get('/{book_id}')
async def view_a_book(book_id) -> dict:
    book_id = int(book_id)
    for book in bookshelf:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not Found')

@book_router.patch('/{book_id}')
async def update_book(book_id, book_update_data:BookUpdate) -> dict:
    book_id = int(book_id)
    for book in bookshelf:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['author'] = book_update_data.author
            book['genre'] = book_update_data.genre
            book['year'] = book_update_data.year
            book['isbn'] = book_update_data.isbn
            book['available'] = book_update_data.available
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not Found')

@book_router.delete('/{book_id}')
async def delete_book(book_id) -> None:
    book_id = int(book_id)
    for book in bookshelf:
        if book['id'] == book_id:
            bookshelf.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book Not Found')