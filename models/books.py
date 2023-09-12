from typing import Optional
from pydantic import BaseModel, Field


class Book(BaseModel):
    id: str = Field(alias="_id")
    title: str
    author: str
    synopsis: str

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }


class BookCreate(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }


class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "Don Quixote is a Spanish novel by Miguel de Cervantes..."
            }
        }
