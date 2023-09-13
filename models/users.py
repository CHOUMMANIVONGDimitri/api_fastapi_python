from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: str = Field(alias="_id")
    username: str
    password: str
    email: str

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "johndoe@domain.com",
                "password": "hashed password..."
            }
        }


class UserCreate(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(..., description="email de l'utilisateur")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "johndoe@domain.com",
                "password": "your password..."
            }
        }


class UserUpdate(BaseModel):
    username: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]

    class Config:
        json_schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "johndoe@domain.com",
                "password": "your password..."
            }
        }
