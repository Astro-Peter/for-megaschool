from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


from schemas import Item

@app.post("/items/")
async def create_item(item: Item):
    return item
