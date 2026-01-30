from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/items/")
async def create_item(item: dict):
    return {"message": "Item created", "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}

# Include routers
from routers.item_router import router as item_router
app.include_router(item_router)