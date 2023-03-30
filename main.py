from typing import Union
from fastapi import FastAPI


# Initialize FastAPI App
app = FastAPI()

@app.get("/books")
def read_books():
    return {
        "books" : "read books"
    }


@app.get("/books")
def post_books():
    return {
        "books" : "post a book"
    } 


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