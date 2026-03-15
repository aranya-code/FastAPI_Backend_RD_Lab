from pydantic import BaseModel, Field

# Using pydantic validation schema for users
class CreateUsers(BaseModel):
    email: str
    username: str
    name: str
    password: str
    role: str

# Using pydanctic validation schema for Todos
class Todos(BaseModel):
    title: str = Field(min_length= 3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    status: bool