import os
from fastapi import FastAPI
from typing import Optional  # optional value
import uvicorn
from pydantic import BaseModel

app = FastAPI()  # To launch type : uvicorn api:app --reload


# Models :

class Items(BaseModel):
    quantity: Optional[int]
    description: Optional[str]

# Routes :

# GET


@app.get("/")
async def hello_world():
    return {"hello": "world"}


@app.get("/item/{id_item}")
async def get_item(id_item: int, quantity: Optional[int] = None, description: Optional[str] = None):
    return {"id": id_item, "quantity": quantity, "description": description}

# POST


@app.post("/item/")
async def post_item(item: Items):
    # request treatement
    return {"id": 1, "item": item.model_dump()}

# Launch server
if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
