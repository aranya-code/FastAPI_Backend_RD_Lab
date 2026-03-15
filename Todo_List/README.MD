# 📝 FastAPI Todo List API

A **RESTful Todo List API** built using **FastAPI, SQLAlchemy, and SQLite**.
This project demonstrates backend concepts like **CRUD operations, database integration, API validation, and automated testing**.

It is designed as a **learning project for building modern Python backend APIs using FastAPI**.

---

# 🚀 Features

* Create Todo items
* Retrieve all Todos
* Retrieve a Todo by ID
* Update Todo items
* Delete Todo items
* Data validation using **Pydantic**
* Database integration using **SQLAlchemy ORM**
* API testing using **Pytest**
* Interactive API documentation using **Swagger UI**

---

# 🛠 Tech Stack

| Technology | Purpose                               |
| ---------- | ------------------------------------- |
| FastAPI    | High performance Python API framework |
| Python     | Backend programming language          |
| SQLAlchemy | ORM for database interaction          |
| SQLite     | Lightweight database                  |
| Pydantic   | Data validation and serialization     |
| Pytest     | API testing framework                 |
| Uvicorn    | ASGI server for running FastAPI       |

---

# 📂 Project Structure

```
Todo_List
│
├── main.py          # FastAPI application & API routes
├── models.py        # SQLAlchemy database models
├── schema.py        # Pydantic schemas
├── database.py      # Database configuration
├── test_main.py     # API test cases
└── requirements.txt # Project dependencies
```

---


# 📚 API Documentation

FastAPI automatically generates interactive API docs.

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

| Method | Endpoint             | Description              |
| ------ | -------------------- | ------------------------ |
| GET    | `/`                  | Retrieve all todos       |
| GET    | `/todos/{id}`        | Retrieve a specific todo |
| POST   | `/todos/create`      | Create a new todo        |
| PUT    | `/todos/update/{id}` | Update a todo            |
| DELETE | `/todos/delete/{id}` | Delete a todo            |

---

# 📦 Example Request

```
POST /todos/create
```

Request body

```json
{
  "title": "Learn FastAPI",
  "description": "Practice building APIs",
  "priority": 3,
  "status": false
}
```

---

# 🧪 Running Tests

Run API tests using **pytest**

```
pytest -v
```

This will run all tests defined in `test_main.py`.

---

# 🎯 Learning Objectives

This project demonstrates:

* REST API development using FastAPI
* Database integration using SQLAlchemy
* Data validation with Pydantic
* Writing automated API tests using Pytest
* Structuring a backend API project

---

# 👨‍💻 Author

**Aranya Majumdar**

GitHub
https://github.com/aranya-code
