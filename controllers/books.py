from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from bson import ObjectId

from models.books import Book, BookUpdate, BookCreate

router = APIRouter()


@router.post("/", response_description="Create a new book", status_code=status.HTTP_201_CREATED, response_model=Book)
def create_book(request: Request, book: BookCreate = Body(...)):
    book = jsonable_encoder(book)
    new_book = request.app.database["books"].insert_one(book)
    created_book = request.app.database["books"].find_one(
        {"_id": new_book.inserted_id}
    )
    created_book['_id'] = str(created_book["_id"])
    return created_book


@router.get("/", response_description="List all books", response_model=List[Book])
def list_books(request: Request, skip: int = 0, limit: int = 100):
    books = list(request.app.database["books"].find().skip(skip).limit(limit))

    for book in books:
        book['_id'] = str(book['_id'])

    return books


@router.get("/{id}", response_description="Get a single book by id", response_model=Book)
def find_book(id: str, request: Request):
    if (book := request.app.database["books"].find_one({"_id": ObjectId(id)})) is not None:
        book['_id'] = id
        return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with ID {id} not found")


@router.put("/{id}", response_description="Update a book", response_model=Book)
def update_book(id: str, request: Request, book: BookUpdate = Body(...)):
    request.app.database["books"].update_one(
        {"_id": ObjectId(id)}, {"$set": dict(book)}
    )

    updated_book = request.app.database["books"].find_one(
        {"_id": ObjectId(id)})
    updated_book['_id'] = id

    if updated_book:
        return updated_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with ID {id} not found")


@router.delete("/{id}", response_description="Delete a book")
def delete_book(id: str, request: Request, response: Response):
    delete_result = request.app.database["books"].delete_one(
        {"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Book with ID {id} not found")
