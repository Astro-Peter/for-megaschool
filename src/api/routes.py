from fastapi import APIRouter

# Initialize the API router
router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@router.post("/items/")
async def create_item(item: dict):
    return {"item": item}