import pytest
from fastapi.testclient import TestClient
from main import app
from routers.auth import get_current_user

client = TestClient(app)


# -------------------------
# MOCK AUTH USER
# -------------------------
def override_get_current_user():
    class User:
        id = 1
    return User()

app.dependency_overrides[get_current_user] = override_get_current_user


# -------------------------
# GET ALL TODOS
# -------------------------
def test_get_all_todos():
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# -------------------------
# CREATE TODO
# -------------------------
def test_create_todo_success():
    data = {
        "title": "Test Todo",
        "description": "Testing",
        "priority": 3,
        "status": False
    }

    response = client.post("/todos/create", json=data)
    assert response.status_code == 201

    body = response.json()
    assert body["title"] == data["title"]
    assert body["priority"] == 3


def test_create_todo_invalid():
    data = {
        "title": "",  # invalid
        "description": "bad",
        "priority": "high",  # invalid type
        "status": False
    }

    response = client.post("/todos/create", json=data)
    assert response.status_code == 422


# -------------------------
# GET TODO BY ID
# -------------------------
def test_get_todo_by_id_not_found():
    response = client.get("/todos/9999")
    assert response.status_code == 404


# -------------------------
# UPDATE TODO
# -------------------------
def test_update_todo_not_found():
    data = {
        "title": "Updated",
        "description": "Updated desc",
        "priority": 2,
        "status": True
    }

    response = client.put("/todos/update/9999", json=data)
    assert response.status_code == 404


# -------------------------
# DELETE TODO
# -------------------------
def test_delete_todo_not_found():
    response = client.delete("/todos/delete/9999")
    assert response.status_code in [200, 404]  # depends on your logic


# -------------------------
# AUTH TEST (IMPORTANT)
# -------------------------
def test_unauthorized_access():
    app.dependency_overrides = {}  # remove mock

    response = client.get("/")
    assert response.status_code == 401

    # restore mock
    app.dependency_overrides[get_current_user] = override_get_current_user


# -------------------------
# EDGE CASES
# -------------------------
def test_empty_payload():
    response = client.post("/todos/create", json={})
    assert response.status_code == 422


def test_large_input():
    data = {
        "title": "A" * 500,
        "description": "B" * 2000,
        "priority": 1,
        "status": False
    }

    response = client.post("/todos/create", json=data)
    assert response.status_code in [201, 422]