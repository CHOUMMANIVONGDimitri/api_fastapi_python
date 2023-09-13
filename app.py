import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from config.db import *
from controllers.books import router as book_router
from controllers.users import router as user_router

load_dotenv()
app = FastAPI()

PORT = os.getenv("PORT")
HOST = os.getenv("HOST")


@app.get("/")
async def get_welcome_message():
    return "Welcome to the API"

app.include_router(book_router, tags=["books"], prefix="/book")
app.include_router(user_router, tags=["users"], prefix="/users")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
