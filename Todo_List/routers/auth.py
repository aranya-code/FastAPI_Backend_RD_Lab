from schema import CreateUsers
from models import Users
from passlib.context import CryptContext
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter()

bcrypt_context = CryptContext(schemes= ['bcrypt'], deprecated= 'auto')

# Fetching database
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creating database dependency
db_dependency = Annotated[Session, Depends(get_db)]

@router.get('/auth/')
def get_user(db: db_dependency):
    return db.query(Users).all()

@router.post('/auth/create_user')
def create_user(db: db_dependency, create_request: CreateUsers):
    create_user_model = Users(
        email = create_request.email,
        username = create_request.username,
        name = create_request.name,
        hashed_password = bcrypt_context.hash(create_request.password),
        role = create_request.role,
        is_active = True
    )

    db.add(create_user_model)
    db.commit()
    return create_user_model

