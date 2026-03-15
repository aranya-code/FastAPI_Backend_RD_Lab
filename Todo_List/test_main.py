from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models
from database import Base
from main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_todos.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def create_test_todo():
    db = TestingSessionLocal()
    todo = models.Todos_Model(
        title="Learn FastAPI",
        description="Practice CRUD testing",
        priority=3,
        status=False
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    db.close()
    return todo


def test_read_all_todos_empty():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo():
    data = {
        "title": "Write tests",
        "description": "Create pytest test cases",
        "priority": 4,
        "status": False
    }

    response = client.post("/todos/create", json=data)

    assert response.status_code == 201
    assert response.json() == data

    check = client.get("/")
    assert check.status_code == 200
    assert len(check.json()) == 1
    assert check.json()[0]["title"] == "Write tests"


def test_read_todo_by_id():
    todo = create_test_todo()

    response = client.get(f"/todos/{todo.id}")

    assert response.status_code == 200
    assert response.json()["id"] == todo.id
    assert response.json()["title"] == "Learn FastAPI"


def test_read_todo_by_id_not_found():
    response = client.get("/todos/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}


def test_update_todo():
    todo = create_test_todo()

    updated_data = {
        "title": "Learn FastAPI Updated",
        "description": "Practice CRUD testing updated",
        "priority": 5,
        "status": True
    }

    response = client.put(f"/todos/update/{todo.id}", json=updated_data)

    assert response.status_code == 204

    check = client.get(f"/todos/{todo.id}")
    assert check.status_code == 200
    assert check.json()["title"] == "Learn FastAPI Updated"
    assert check.json()["description"] == "Practice CRUD testing updated"
    assert check.json()["priority"] == 5
    assert check.json()["status"] is True


def test_update_todo_not_found():
    updated_data = {
        "title": "Missing Todo",
        "description": "This should fail",
        "priority": 2,
        "status": False
    }

    response = client.put("/todos/update/999", json=updated_data)

    assert response.status_code == 404
    assert response.json() == {"detail": "No todo found"}


def test_delete_todo():
    todo = create_test_todo()

    response = client.delete(f"/todos/delete/{todo.id}")
    assert response.status_code in [200, 204]

    check = client.get("/")
    assert check.status_code == 200
    assert len(check.json()) == 0


def test_create_todo_validation_error_short_title():
    data = {
        "title": "ab",
        "description": "Valid description",
        "priority": 3,
        "status": False
    }

    response = client.post("/todos/create", json=data)
    assert response.status_code == 422


def test_create_todo_validation_error_invalid_priority():
    data = {
        "title": "Valid Title",
        "description": "Valid description",
        "priority": 10,
        "status": False
    }

    response = client.post("/todos/create", json=data)
    assert response.status_code == 422