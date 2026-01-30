from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}
from fastapi import FastAPI
from src.routes import items

app.include_router(items.router)