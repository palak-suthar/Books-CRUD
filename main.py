
from fastapi import FastAPI

app = FastAPI()

# Temporary book storage
books = [
    {"id": 1, "title": "Python Basics", "author": "John"},
    {"id": 2, "title": "Data Science", "author": "David"}
]

@app.get("/")
def home():
    return {"message": "Books CRUD API is running"}

# 1. CREATE - Add a new book
@app.post("/books")
def add_book(book: dict):
    books.append(book)
    return {
        "message": "Book added successfully",
        "book": book
    }


# 2. READ - Get all books
@app.get("/books")
def get_books():
    return books


# 3. READ - Get book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    return {"message": "Book not found"}


# 4. UPDATE - Update book details
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book["title"]
            book["author"] = updated_book["author"]

            return {"message": "Book updated successfully"}

    return {"message": "Book not found"}


# 5. DELETE - Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}

    return {"message": "Book not found"}
