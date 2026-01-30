from typing import List, Optional
from datetime import datetime
import uuid
from ..models.item import Item, ItemCreate, ItemUpdate

# Mock storage for items (in a real application, this would be a database)
items_db = []

def get_item(item_id: int) -> Optional[Item]:
    """Get an item by ID"""
    for item in items_db:
        if item.id == item_id:
            return item
    return None

def get_items(skip: int = 0, limit: int = 100) -> List[Item]:
    """Get a list of items with pagination"""
    return items_db[skip:skip + limit]

def create_item(item: ItemCreate) -> Item:
    """Create a new item"""
    db_item = Item(
        id=len(items_db) + 1,
        name=item.name,
        description=item.description,
        price=item.price,
        tax=item.tax,
        created_at=datetime.now()
    )
    items_db.append(db_item)
    return db_item

def update_item(item_id: int, item: ItemUpdate) -> Optional[Item]:
    """Update an existing item"""
    for i, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            updated_data = item.dict(exclude_unset=True)
            items_db[i] = Item(
                id=existing_item.id,
                created_at=existing_item.created_at,
                **updated_data
            )
            return items_db[i]
    return None

def delete_item(item_id: int) -> bool:
    """Delete an item by ID"""
    global items_db
    original_length = len(items_db)
    items_db = [item for item in items_db if item.id != item_id]
    return len(items_db) < original_length