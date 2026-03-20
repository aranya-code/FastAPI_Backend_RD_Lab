from fastapi import APIRouter, HTTPException, status, Depends
from models import Users
from sqlalchemy.orm import Session
from typing import Annotated
from database import SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext
from schema import user_verification


# Creating router for users
router = APIRouter(
    prefix='/user',
    tags=['user']
)

# Fetching database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creating dependencies
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

# Get user details
@router.get('/details')
def get_user(db: db_dependency, user: user_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_profile = db.query(Users).filter(Users.username == user.username).first()
    return user_profile

# Change password
@router.put('/password', status_code=status.HTTP_200_OK)
def change_password(db: db_dependency, user: user_dependency, user_verification: user_verification):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_model = db.query(Users).filter(Users.id == user.id).first()
    
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail= 'Could not authenticate user')
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()