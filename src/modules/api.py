from fastapi import APIRouter

router = APIRouter()

# In-memory storage for items
items = []

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@router.get("/items/")
async def get_items():
    return items

@router.post("/items/")
async def create_item(item: dict):
    item_id = len(items) + 1
    item['item_id'] = item_id
    items.append(item)
    return {"item": item}

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    global items
    items = [item for item in items if item['item_id'] != item_id]
    return {"message": f"Item {item_id} deleted"}
