from fastapi import FastAPI

app = FastAPI()

# Sample route
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
from models import Item

async def create_item(item: Item):
    return {"item": item}