import os
from fastapi import FastAPI
import uvicorn
import certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from controllers.books.index import router as book_router

load_dotenv()
app = FastAPI()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE = os.getenv("DATABASE")
PORT = os.getenv("PORT")
HOST = os.getenv("HOST")


client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")

    # Check if the database exists
    if DATABASE not in client.list_database_names():
        app.database = client[DATABASE]
        # Create a default collection to trigger database creation
        app.database.create_collection("users")
        print(f"Database '{DATABASE}' created.")
    else:
        app.database = client[DATABASE]
        print(f"Connected to '{DATABASE}' database...")

except Exception as e:
    print(e)


@app.get("/")
async def get_all_items():
    return "Welcome to the API"

app.include_router(book_router, tags=["books"], prefix="/book")


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
