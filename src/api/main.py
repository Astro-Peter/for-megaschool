from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

from fastapi import FastAPI
from .routes.data_routes import router as data_router

app.include_router(data_router, prefix="/api")
