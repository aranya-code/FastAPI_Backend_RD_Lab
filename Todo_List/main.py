from fastapi import FastAPI, Depends, HTTPException, status, Path
from database import engine, SessionLocal
from models import Todos_Model
import models
from typing import Annotated
from sqlalchemy.orm import Session
from schema import Todos

app = FastAPI()

# Defining db connection
models.Base.metadata.create_all(bind=engine)

# Fetching Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creating database dependency
db_dependency = Annotated[Session, Depends(get_db)]

# Get all todos
@app.get('/')
def read_db(db: db_dependency):
    return db.query(Todos_Model).all()

# Get todo by id
@app.get('/todos/{todo_id}', status_code= status.HTTP_200_OK)
def read_by_id(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_list = db.query(Todos_Model).filter(Todos_Model.id==todo_id).first()
    if todo_list is not None:
        return todo_list
    raise HTTPException(status_code= 404, detail= 'Todo not found')

# Create a todo
@app.post('/todos/create', status_code= status.HTTP_201_CREATED)
def create_todo(db: db_dependency, todo_request: Todos):
    todo_item = Todos_Model(**todo_request.model_dump())
    db.add(todo_item)
    db.commit()
    return todo_request

# Update a todo
@app.put('/todos/update/{todo_id}', status_code= status.HTTP_204_NO_CONTENT)
def update_todo(db: db_dependency, todo_id: int, todo_request: Todos):
    todo_item = db.query(Todos_Model).filter(Todos_Model.id == todo_id).first()
    if todo_item is None:
        raise HTTPException(status_code=404, detail='No todo found')
    todo_item.title = todo_request.title
    todo_item.description = todo_request.description
    todo_item.priority = todo_request.priority
    todo_item.status = todo_request.status

    db.add(todo_item)
    db.commit()

# Delete a todo
@app.delete('/todos/delete/{todo_id}')
def delete_todo(db: db_dependency, todo_id: int):
    todo_item = db.query(Todos_Model).filter(Todos_Model.id == todo_id)
    todo_item.delete()
    db.commit()
    
