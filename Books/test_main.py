import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test: Get all books
def test_get_all_books():
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test: Get book by ID
def test_get_book_by_id():
    response = client.get("/books/id/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


# Test: Book not found
def test_get_book_invalid_id():
    response = client.get("/books/id/999")
    assert response.status_code == 404


# Test: Get book by title
def test_get_book_by_title():
    response = client.get("/books/title/Title One")
    assert response.status_code == 200
    assert response.json()["title"] == "Title One"


# Test: Filter by rating
def test_get_book_by_rating():
    response = client.get("/books/rating?rating=3")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test: Create book
def test_create_book():
    new_book = {
        "title": "Test Book",
        "author": "Test Author",
        "category": "science",
        "rating": 8,
        "published_year": 2020
    }

    response = client.post("/books/create_book", json=new_book)

    assert response.status_code == 200
    assert response.json()["book"]["title"] == "Test Book"


# Test: Update book
def test_update_book():
    updated_book = {
        "id": 1,
        "title": "Updated Title",
        "author": "Updated Author",
        "category": "science",
        "rating": 9,
        "published_year": 2020
    }

    response = client.put("/books/update_book?title=Title One", json=updated_book)

    assert response.status_code == 200
    assert response.json()["message"] == "Book updated successfully"


# Test: Delete book
def test_delete_book():
    response = client.delete("/books/delete?title=Updated Title")
    assert response.status_code == 200 or response.status_code == 204