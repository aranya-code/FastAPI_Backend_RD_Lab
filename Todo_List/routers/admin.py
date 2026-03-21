from fastapi import APIRouter, Depends, HTTPException, status
from models import Users, Todos_Model
from typing import Annotated
from .auth import get_current_user
from database import SessionLocal
from sqlalchemy.orm import Session


# Creating router path
router = APIRouter(prefix= '/admin',tags=['admin'])

# Fetching database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Creating dependency
db_dependency = Annotated[Session, Depends(get_db)]
user_depenedency = Annotated[dict, Depends(get_current_user)]

# Get all users
@router.get('/users', status_code= status.HTTP_200_OK)
def get_users(db: db_dependency, user: user_depenedency):
    if user is None or user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    users= db.query(Users).all()
    return users



# Get all Todos
@router.get('/todos', status_code= status.HTTP_200_OK)
def get_todos(db: db_dependency, user: user_depenedency):
    if user is None or user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = 'Authentication failed')
    return db.query(Todos_Model).all()

# Delete Todo by id
@router.post('/todo/{todo_id}')
def delete_todo_by_id(db: db_dependency, user: user_depenedency, todo_id):
    if user is None or user.role != 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    item = db.query(Todos_Model).filter(Todos_Model.id == todo_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail='No todo found')
    db.delete(item)
    db.commit()
