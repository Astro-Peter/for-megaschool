from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items_db = []  # In-memory database

@router.post("/items/", response_model=Item)
async def create_item(item: Item):
    items_db.append(item)
    return item

@router.get("/items/", response_model=List[Item])
async def read_items():
    return items_db

# You can add more CRUD operations as needed.