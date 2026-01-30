from fastapi import APIRouter
from ..models.data_model import DataModel

router = APIRouter()

# In-memory data storage as an example
fake_db = []

@router.post("/data/")
async def create_data(item: DataModel):
    fake_db.append(item)
    return item

@router.get("/data/{item_id}")
async def read_data(item_id: int):
    return fake_db[item_id]

@router.get("/data/")
async def read_all_data():
    return fake_db
