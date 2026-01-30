from fastapi import FastAPI
from models.item import Item

app = FastAPI()

@app.get("/",
    summary="Root endpoint",
    description="A simple welcome endpoint.")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/items/",
    summary="Create an item",
    description="Create a new item with the given details.")
async def create_item(item: Item):
    return {"item": item, "message": "Item created!"}