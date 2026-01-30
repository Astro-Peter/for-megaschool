from fastapi import APIRouter
from models.item import Item

router = APIRouter()

@router.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created", "item": item}

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"message": "Item found", "item_id": item_id}

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}