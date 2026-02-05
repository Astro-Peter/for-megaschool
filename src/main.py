from fastapi import FastAPI
from src.api.router import router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

app.include_router(router)

# Run the app using the following command:
# uvicorn src.main:app --reload

# Automatic API documentation with Swagger UI is provided by FastAPI.
