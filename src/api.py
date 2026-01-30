from fastapi import FastAPI

app = FastAPI()

# Sample data structure
items = []

@app.get("/items")
async def read_items():
    return items

@app.post("/items")
async def create_item(item: dict):
    items.append(item)
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return items[item_id]

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return items.pop(item_id)