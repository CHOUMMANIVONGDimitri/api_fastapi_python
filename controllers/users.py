from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from bson import ObjectId
from config.db import db

from models.users import User, UserCreate, UserUpdate

router = APIRouter()

Users = db['users']


@router.post("/register", response_description="Create a new user", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(request: Request, user: UserCreate = Body(...)):
    user = jsonable_encoder(user)

    if (Users.find_one({"email": user['email']})) is None:
        new_user = Users.insert_one(user)
        created_user = Users.find_one(
            {"_id": new_user.inserted_id}
        )
        created_user['_id'] = str(created_user["_id"])
        return created_user

    raise HTTPException(status_code=status.HTTP_409_CONFLICT)


@router.get("/", response_description="List all users", response_model=List[User])
def list_users(request: Request, skip: int = 0, limit: int = 100):
    users = list(Users.find().skip(skip).limit(limit))

    for user in users:
        user['_id'] = str(user['_id'])

    return users


@router.get("/{id}", response_description="Get a single user by id", response_model=User)
def find_user(id: str, request: Request):
    if (user := Users.find_one({"_id": ObjectId(id)})) is not None:
        user['_id'] = id
        return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with ID {id} not found")


@router.put("/{id}", response_description="Update a user", response_model=User)
def update_user(id: str, request: Request, book: UserUpdate = Body(...)):
    Users.update_one(
        {"_id": ObjectId(id)}, {"$set": dict(book)}
    )

    updated_user = Users.find_one(
        {"_id": ObjectId(id)})
    updated_user['_id'] = id

    if updated_user:
        return updated_user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with ID {id} not found")


@router.delete("/{id}", response_description="Delete a user")
def delete_user(id: str, request: Request, response: Response):
    delete_result = Users.delete_one(
        {"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with ID {id} not found")
