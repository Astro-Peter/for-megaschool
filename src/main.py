from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

@app.post('/users/')
async def create_user(user: User):
    return user

@app.get('/users/{user_id}')
async def get_user(user_id: int):
    return User(id=user_id, name='Sample User', email='sample@example.com')