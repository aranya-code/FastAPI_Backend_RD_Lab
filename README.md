# 🚀 FastAPI Backend RD Lab

A collection of backend projects built using FastAPI, demonstrating the progression from basic API development to a structured, authentication-based backend system.

---

## Infrastructure & Automation
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)
[![Books CI](https://github.com/aranya-code/FastAPI_Backend_RD_Lab/actions/workflows/books-ci.yml/badge.svg)](https://github.com/aranya-code/FastAPI_Backend_RD_Lab/actions/workflows/books-ci.yml)

[![Books CI](https://github.com/aranya-code/FastAPI_Backend_RD_Lab/actions/workflows/books-ci.yml/badge.svg?v=1)](https://github.com/aranya-code/FastAPI_Backend_RD_Lab/actions/workflows/books-ci.yml)

* **Containerization:** Fully containerized using `Docker` and `docker-compose` for consistent multi-environment deployments.
* **CI/CD Pipeline:** Automated GitHub Actions workflows configured with path-filtering to independently run Pytest and Flake8 linting for isolated micro-projects.

## Quick Start
Spin up the entire environment (API and Database) in one command:
`docker-compose up --build`

## 📌 Overview

This repository contains **two FastAPI projects** showcasing different levels of backend development:

1. 📚 **Books API (Beginner Level)**  
2. ✅ **Todo API (Intermediate Level with Authentication & Database)**  

The goal of this repository is to demonstrate practical backend concepts such as:
- API design
- Data validation
- Authentication
- Database integration
- Modular architecture

---

## 🧩 Projects Included

---

### 📚 1. Books API (Beginner)

A simple REST API built using FastAPI with in-memory data storage.

#### 🔹 Features
- CRUD operations for books
- Request validation using Pydantic
- Path & query parameter handling
- Basic API structure

#### 🔹 Tech Used
- FastAPI
- Pydantic

#### 🔹 Purpose
This project focuses on learning:
- FastAPI routing
- Request/response handling
- Basic API design

---

### ✅ 2. Todo API (Intermediate)

A more advanced backend system with authentication and database integration.

#### 🔹 Features
- JWT-based authentication
- User-specific todos (owner-based access)
- Full CRUD operations
- SQLAlchemy ORM integration
- Dependency injection
- Modular router-based structure
- Testable API design

#### 🔹 Tech Used
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Pytest

#### 🔹 Architecture Highlights
- Separation of concerns (models, schemas, routers)
- Dependency injection for DB and authentication
- Secure endpoints with user validation

---


---

### 4. Run the server
uvicorn main:app --reload


---

## 📄 API Documentation

FastAPI provides built-in interactive docs:

- Swagger UI → http://127.0.0.1:8000/docs  

---

## 🔒 Authentication (Todo API)

All todo endpoints are protected.


---

## 🧪 Running Tests
pytest -v


---

## 📈 Learning Progression

This repository demonstrates:

- Beginner → CRUD API with in-memory data
- Intermediate → Authentication + database + modular design

---

## 🚀 Future Improvements

- Convert routes to RESTful design (`/todos/{id}`)
- Add response models for better API control
- Implement pagination and filtering
- Add Docker support
- Deploy to cloud (AWS / Render / Railway)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Push and create a Pull Request  

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Aranya Majumdar**



