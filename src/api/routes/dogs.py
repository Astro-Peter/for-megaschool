from typing import List
from fastapi import APIRouter, HTTPException, status
from ..models.dog import Dog, DogCreate, DogUpdate
from ..services.dogs import get_dog, get_dogs, create_dog, update_dog, delete_dog

router = APIRouter(prefix="/dogs", tags=["dogs"])

@router.post("/", response_model=Dog, status_code=status.HTTP_201_CREATED)
async def create_dog_endpoint(dog: DogCreate):
    return create_dog(dog)


@router.get("/{dog_id}", response_model=Dog)
async def read_dog(dog_id: int):
    db_dog = get_dog(dog_id)
    if not db_dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog


@router.get("/", response_model=List[Dog])
async def read_dogs(skip: int = 0, limit: int = 100):
    return get_dogs(skip=skip, limit=limit)


@router.put("/{dog_id}", response_model=Dog)
async def update_dog_endpoint(dog_id: int, dog: DogUpdate):
    db_dog = update_dog(dog_id, dog)
    if not db_dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog


@router.delete("/{dog_id}")
async def delete_dog_endpoint(dog_id: int):
    deleted = delete_dog(dog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Dog not found")
    return {"message": "Dog deleted successfully"}