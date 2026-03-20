from fastapi import APIRouter, Depends, HTTPException, status, Path
from database import SessionLocal
from models import Todos_Model
from typing import Annotated
from sqlalchemy.orm import Session
from schema import Todos
from .auth import get_current_user

router = APIRouter()


# Fetching Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creating dependency
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

# Get all todos
@router.get('/')
def read_db(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not Authenticated')   
    return db.query(Todos_Model).filter(Todos_Model.owner_id == user.id).all()

# Get todo by id
@router.get('/todos/{todo_id}', status_code= status.HTTP_200_OK)
def read_by_id(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not Authenticated')
    todo_list = db.query(Todos_Model).filter(Todos_Model.id==todo_id)\
        .filter(Todos_Model.owner_id == user.id).first()
    if todo_list is not None:
        return todo_list
    raise HTTPException(status_code= 404, detail= 'Todo not found')

# Create a todo
@router.post('/todos/create', status_code= status.HTTP_201_CREATED)
def create_todo(user: user_dependency, db: db_dependency, todo_request: Todos):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not Authenticated')
    todo_item = Todos_Model(**todo_request.model_dump(), owner_id = user.id)
    db.add(todo_item)
    db.commit()
    return todo_request

# Update a todo
@router.put('/todos/update/{todo_id}', status_code= status.HTTP_204_NO_CONTENT)
def update_todo(user: user_dependency, db: db_dependency, todo_id: int, todo_request: Todos):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not Authenticated')
    todo_item = db.query(Todos_Model).filter(Todos_Model.id == todo_id)\
        .filter(Todos_Model.owner_id == user.id).first()
    if todo_item is None:
        raise HTTPException(status_code=404, detail='No todo found')
    todo_item.title = todo_request.title
    todo_item.description = todo_request.description
    todo_item.priority = todo_request.priority
    todo_item.status = todo_request.status

    db.add(todo_item)
    db.commit()

# Delete a todo
@router.delete('/todos/delete/{todo_id}')
def delete_todo(user: user_dependency, db: db_dependency, todo_id: int):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Not Authenticated')
    todo_item = db.query(Todos_Model).filter(Todos_Model.id == todo_id)\
        .filter(Todos_Model.owner_id == user.id).first()
    db.delete(todo_item)
    db.commit()
    
