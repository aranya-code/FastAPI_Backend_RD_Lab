from pydantic import BaseModel, Field

# Using pydantic validation schema for users
class CreateUsers(BaseModel):
    email: str
    username: str
    name: str
    password: str
    role: str

# Using pydantic validation schema for token
class Token(BaseModel):
    access_token: str
    token_type: str

# Using pydanctic validation schema for Todos
class Todos(BaseModel):
    title: str = Field(min_length= 3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    status: bool

# Using pydantic validation schema for password
class user_verification(BaseModel):
    password: str
    new_password: str = Field(min_length=5)