from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DogBase(BaseModel):
    name: str
    breed: str
    age: Optional[int] = None


class DogCreate(DogBase):
    pass


class DogUpdate(DogBase):
    name: Optional[str] = None
    breed: Optional[str] = None
    age: Optional[int] = None


class Dog(DogBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True