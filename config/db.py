import os
import certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE = os.getenv("DATABASE")

client = MongoClient(MONGODB_URI, tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")

    # Check if the database exists
    if DATABASE not in client.list_database_names():
        db = client[DATABASE]
        # Create a default collection to trigger database creation
        db.create_collection("users")
        print(f"Database '{DATABASE}' created.")
    else:
        db = client[DATABASE]
        print(f"Connected to '{DATABASE}' database...")

except Exception as e:
    print(e)
