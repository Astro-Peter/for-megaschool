from typing import List
from fastapi import APIRouter, HTTPException, status
from ..models.item import Item, ItemCreate, ItemUpdate
from ..services.items import get_item, get_items, create_item, update_item, delete_item

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item_endpoint(item: ItemCreate):
    """Create a new item"""
    return create_item(item)


@router.get("/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """Read an item by ID"""
    db_item = get_item(item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.get("/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 100):
    """Get a list of items with pagination"""
    return get_items(skip=skip, limit=limit)


@router.put("/{item_id}", response_model=Item)
async def update_item_endpoint(item_id: int, item: ItemUpdate):
    """Update an existing item"""
    db_item = update_item(item_id, item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.delete("/{item_id}")
async def delete_item_endpoint(item_id: int):
    """Delete an item"""
    deleted = delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}