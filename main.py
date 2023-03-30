from typing import Union
from fastapi import FastAPI
from model import Book, session

# Initialize FastAPI App
app = FastAPI()

@app.get("/books")
def read_books():
    book = Book()
    session.add(book)
    session.commit()

    return {"books" : "read books"}, 200


@app.get("/books")
def post_books():
    book_query = session.query(Book)
    return book_query.all(), 200
    


@app.get("/books/{book_id}")
def read_book(book_id:int, q:Union[str, None] = None):
    return {
        "book" : f"Read book with id: {book_id}"
    }

@app.put("/books/{book_id}")
def update_book(book_id:int, q:Union[str, None] = None):
    return {
        "book" : f"book with id: {book_id}"
    }

@app.delete("/books/{book_id}")
def delete_book(book_id:int, q:Union[str, None] = None):
    return {
        "book" : f"book with id: {book_id}"
    }