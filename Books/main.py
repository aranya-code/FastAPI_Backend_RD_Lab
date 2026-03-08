# Import required FastAPI modules
from fastapi import FastAPI, Body, Path, Query, HTTPException

# Import the Book schema (Pydantic model) for validation
from schema import Book

# Create FastAPI application instance
app = FastAPI()

# In-memory database (list of dictionaries)
# This acts as a temporary data store for books
BOOKS = [
  { "id": 1, "title": "Title One",   "author": "Author One",   "category": "science", "rating": 3, "published_year": 2014 },
  { "id": 2, "title": "Title Two",   "author": "Author Two",   "category": "science", "rating": 3, "published_year": 2019 },
  { "id": 3, "title": "Title Three", "author": "Author Three", "category": "history", "rating": 7, "published_year": 2024 },
  { "id": 4, "title": "Title Four",  "author": "Author Four",  "category": "math",    "rating": 6, "published_year": 2025 },
  { "id": 5, "title": "Title Five",  "author": "Author Five",  "category": "math",    "rating": 5, "published_year": 2026 },
  { "id": 6, "title": "Title Six",   "author": "Author Two",   "category": "math",    "rating": 9, "published_year": 2017 }
]


# Root endpoint - returns all books
@app.get('/')
def get_books():
    return BOOKS


# Get book by title
# Path parameter: book_title
@app.get('/books/title/{book_title}')
def book_by_title(book_title: str):

    # Iterate through books and match title (case insensitive)
    for book in BOOKS:
        if book.get('title').capitalize() == book_title.capitalize():
            return book


# Get book by ID
# Path parameter validation ensures ID must be greater than 0
@app.get('/books/id/{book_id}')
def book_by_id(book_id: int = Path(gt=0)):

    # Search for the book with matching ID
    for book in BOOKS:
        if book['id'] == book_id:
            return book

    # Raise error if book is not found
    raise HTTPException(status_code=404, detail='Book is not found')


# Get books by rating
# Query parameter validation ensures rating is between 1 and 9
@app.get('/books/rating')
def book_by_rating(rating: int = Query(gt=0, lt=10)):

    # Return all books with matching rating
    return [book for book in BOOKS if book['rating'] == rating]


# Get books by category
@app.get('/books/category/{category}')
def book_by_category(category: str):

    # Filter books by category (case insensitive)
    return [book for book in BOOKS if book['category'].capitalize() == category.capitalize()]


# Get book by author name
@app.get('/books/author/{author}')
def book_by_author(author: str):

    # Search for the first book by the author
    for book in BOOKS:
        if book['author'].capitalize() == author.capitalize():
            return book

    # Return message if no book found
    return HTTPException(status_code = 404, detail= 'No book available')


# Get books by published year
# Year must be between 1948 and 2025
@app.get('/books/published_year/{year}')
def book_by_year(year: int = Path(gt=1947, lt=2026)):

    # Filter books by published year
    return [book for book in BOOKS if book['published_year'] == year]


# Create a new book
# Uses Pydantic Book schema for validation
@app.post('/books/create_book')
def create_book(new_book: Book):

    # Convert Pydantic model to dictionary
    new_book = new_book.model_dump()

    # Automatically generate ID
    new_book['id'] = len(BOOKS) + 1

    # Add new book to the list
    BOOKS.append(new_book)

    # Return success message with created book
    return {
        'message': 'Book created successfully',
        'book': new_book
    }


# Update an existing book by title
@app.put('/books/update_book')
def update_book(title: str, updated_book: dict = Body()):

    # Loop through books to find matching title
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].lower() == title.lower():

            # Replace existing book with updated data
            BOOKS[i] = updated_book

    # Return success message
    return {
        'message': 'Book updated successfully',
        'book': updated_book
    }


# Delete a book by title
@app.delete('/books/delete')
def delete_book(title: str):

    # Loop through books to find matching title
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].lower() == title.lower():

            # Remove book from list
            BOOKS.pop(i)
            break

    # Return confirmation message
    return {"message": "Book deleted successfully"}