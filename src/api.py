from fastapi import FastAPI
from src.models import Item

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item(item: Item):
    return item

from starlette.responses import PlainTextResponse
from middleware import CustomErrorMiddleware
app.add_middleware(CustomErrorMiddleware)

