# 🚀 FastAPI Todo List Backend

A secure and scalable Todo List REST API built using FastAPI, featuring authentication, database integration, and full CRUD operations.

---

## 📌 Overview

This project is a backend API for managing todos with user authentication. It demonstrates:

- Secure user-based access (JWT authentication)
- CRUD operations for todos
- Testable API design
- Automatic API documentation

---

## ⚙️ Features

- User Authentication (JWT-based)
- Create, Read, Update, Delete Todos
- Database integration with SQLAlchemy
- Dependency Injection (FastAPI style)
- Request & Response validation using Pydantic
- Interactive API Docs (/docs, /redoc)
- Modular project structure

---

## 🚀 Quick Access
You can access the deployed version of this application here: 
👉 **[Live Demo on Render](https://fastapi-backend-rd-lab.onrender.com/app)**

*Note: The demo site might take a moment to load if it hasn't been accessed recently.*

---

## 🏗️ Project Structure

```
Todo_List/
│
├── main.py # Entry point
├── database.py # DB connection
├── models.py # SQLAlchemy models
├── schema.py # Pydantic schemas
├── routers/
│ ├── todos.py # Todo endpoints
│ └── auth.py # Authentication
├── tests/ # Test cases
└── requirements.txt

```


---

## 📄 API Documentation

Once running:

- Swagger UI → http://127.0.0.1:8000/docs  
- ReDoc → http://127.0.0.1:8000/redoc  

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|---------|------------|
| POST   | /auth/  | Login & get token |

---

### Todos

| Method | Endpoint | Description |
|--------|---------|------------|
| GET    | /       | Get all todos (user-specific) |
| GET    | /todos/{id} | Get todo by ID |
| POST   | /todos/create | Create new todo |
| PUT    | /todos/update/{id} | Update todo |
| DELETE | /todos/delete/{id} | Delete todo |

---

## 🧪 Running Tests

pytest -v

---

## 🔒 Authentication

This API uses JWT-based authentication.

---


---

## 🧠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Pytest

---

## 📈 Future Improvements

- Convert to RESTful routes (/todos/{id} style)
- Add test database (SQLite for testing)
- Docker support
- Deploy to cloud (Render / AWS / Railway)
- Add pagination & filtering

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo  
2. Create a new branch  
3. Commit your changes  
4. Push and create a PR  

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Aranya Majumdar

