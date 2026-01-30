from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model for User
class User(BaseModel):
    id: int
    name: str
    email: str

# Sample endpoint to create a user
@app.post("/users/")
async def create_user(user: User):
    return {"id": user.id, "name": user.name, "email": user.email}

# Sample endpoint to retrieve a user by ID
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "name": "Sample User", "email": "sample@example.com"}