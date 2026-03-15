from fastapi import FastAPI
from database import engine, SessionLocal
import models
from routers import auth, todos

app = FastAPI()

# Defining db connection
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
