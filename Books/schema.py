from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class Book(BaseModel):
    # Inheriting BaseModel to validate Book model using Pydantic

    id: Optional[int] = None
    title: str
    author: str = Field(min_length=5)
    category: str = Field(max_length=50)
    rating: int = Field(ge=1, le=10)
    published_year: int = Field(gt=1947, le=2026)

    # Configuring model to show in the swagger
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "A new book",
                "author": "New author",
                "category": "Add new category",
                "rating": 9,
                "published_year": "Publishing year"
            }
        }
    )