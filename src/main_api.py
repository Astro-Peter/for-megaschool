from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

# Error handling
@app.exception_handler(Exception)
async def universal_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": str(exc)})