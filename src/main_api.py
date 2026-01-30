from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: dict):
    return item
from models import Item

@app.post("/items/")
async def create_item(item: Item):
    return item
# Error handling
@app.exception_handler(Exception)
async def universal_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": str(exc)})