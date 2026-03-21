from schema import CreateUsers, Token
from models import Users
from passlib.context import CryptContext
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
from datetime import timedelta, datetime
from starlette import status

load_dotenv()

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes= ['bcrypt'], deprecated= 'auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl= '/auth/token')


# Fetching database
def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creating database dependency
db_dependency = Annotated[Session, Depends(get_db)]

# Authenticating user profile
def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

# Creating access token
def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.now() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

# Validating user
def get_current_user(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        role: str = payload.get('role')

        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail= 'Could not validate user')
        
        user = db.query(Users).filter(Users.id == user_id).first()
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail= 'Could not validate user')


# @router.get('/auth/')
# def get_user(db: db_dependency):
#     return db.query(Users).all()

# Creating the user
@router.post('/create_user')
def create_user(db: db_dependency, create_request: CreateUsers):
    create_user_model = Users(
        email = create_request.email,
        username = create_request.username,
        name = create_request.name,
        hashed_password = bcrypt_context.hash(create_request.password),
        role = create_request.role,
        is_active = True,
        phone_number = create_request.phone_number
    )

    db.add(create_user_model)
    db.commit()
    return create_user_model

# Creating token 
@router.post('/token', response_model=Token)
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail= 'Could not validate user')
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}