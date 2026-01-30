from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@router.post("/items/")
async def create_item(item: dict):
    return item
