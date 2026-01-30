
from fastapi import APIRouter
from src.models.item import Item

router = APIRouter()

@router.post("/items/")
async def create_item(item: Item):
    return item