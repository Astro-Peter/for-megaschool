from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

from routers.item_router import router

app.include_router(router)

# To run the application, use `uvicorn src.api.app:app --reload`

# This will allow you to access the API documentation at http://127.0.0.1:8000/docs