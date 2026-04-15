from fastapi import FastAPI
from database import engine, SessionLocal
import models
from routers import auth, todos, admin, users
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

# Defining db connection
models.Base.metadata.create_all(bind=engine)

app.include_router(admin.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/app", response_class=FileResponse)
def serve_frontend():
    return FileResponse("index.html")