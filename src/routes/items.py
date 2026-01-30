from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
async def get_items():
    return []

@router.post("/items/")
async def create_item(item: dict):
    return item

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"item_id": item_id, **item}

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}