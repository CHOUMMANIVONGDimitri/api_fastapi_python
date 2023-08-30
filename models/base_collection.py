from pydantic import BaseModel
from typing import List


class BaseCollection:
    def __init__(self, db, collection_name, model):
        self.collection = db[collection_name]
        self.model = model

    async def insert_one(self, item: BaseModel):
        result = await self.collection.insert_one(item.model_dump())
        return str(result.inserted_id)

    async def find_all(self) -> List[BaseModel]:
        cursor = self.collection.find({})
        items = [self.model(**item) for item in await cursor.to_list(length=None)]
        return items
