from fastapi import FastAPI, Body, Path, Query, HTTPException
from schema import Book

app = FastAPI()

BOOKS = [
  { "id": 1, "title": "Title One",   "author": "Author One",   "category": "science" , "rating": 3, "published_year": 2014 },
  { "id": 2, "title": "Title Two",   "author": "Author Two",   "category": "science" , "rating": 3, "published_year": 2019 },
  { "id": 3, "title": "Title Three", "author": "Author Three", "category": "history" , "rating": 7, "published_year": 2024 },
  { "id": 4, "title": "Title Four",  "author": "Author Four",  "category": "math" , "rating": 6, "published_year": 2025  },
  { "id": 5, "title": "Title Five",  "author": "Author Five",  "category": "math" , "rating": 5, "published_year": 2026  },
  { "id": 6, "title": "Title Six",   "author": "Author Two",   "category": "math" , "rating": 9, "published_year": 2017  }
]


@app.get('/')
def get_books():
    return BOOKS

@app.get('/books/title/{book_title}')
def book_by_title(book_title : str):
    for book in BOOKS:
        if book.get('title').capitalize() == book_title.capitalize():
            return book
        
@app.get('/books/id/{book_id}')
def book_by_id(book_id : int = Path(gt=0)):
    for book in BOOKS:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code = 404, detail = 'Book is not found')
        
@app.get('/books/rating')
def book_by_rating(rating : int = Query(gt=0, lt=10)):
    return [book for book in BOOKS if book['rating'] == rating]


@app.get('/books/category/{category}')
def book_by_category(category : str):
    return[book for book in BOOKS if book['category'].capitalize() == category.capitalize()]


@app.get('/books/author/{author}')
def book_by_author(author : str):
    for book in BOOKS:
        if book['author'].capitalize() == author.capitalize():
            return book
    return 'No Book Available'

@app.get('/books/published_year/{year}')
def book_by_year(year: int = Path(gt=1947, lt=2026)):
    return[book for book in BOOKS if book['published_year'] == year]


@app.post('/books/create_book')
def create_book(new_book : Book):
    new_book = new_book.model_dump()
    new_book['id'] = len(BOOKS)+1  
    BOOKS.append(new_book)
    return {
        'message': 'Book created successfully',
        'book': new_book
    }
        
    
@app.put('/books/update_book')
def update_book(title : str, updated_book: dict= Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].lower() == title.lower():
            BOOKS[i] = updated_book

    return {
        'message': 'Book updated successfully',
        'book': updated_book
    }

@app.delete('/books/delete')
def delete_book(title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i]['title'].lower() == title.lower():
            BOOKS.pop(i)
            break



