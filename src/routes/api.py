from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

api_router = APIRouter()

class Item(BaseModel):
    name: str
    price: float

@api_router.post("/items/")
async def create_item(item: Item):
    if item.price < 0:
        raise HTTPException(status_code=400, detail="Price must be a positive number")
    return item

@api_router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item", "price": 25.0}