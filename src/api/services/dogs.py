from typing import List, Optional
from datetime import datetime
from ..models.dog import Dog, DogCreate, DogUpdate

# Mock storage for dogs (in a real application, this would be a database)
dogs_db = []

def get_dog(dog_id: int) -> Optional[Dog]:
    for dog in dogs_db:
        if dog.id == dog_id:
            return dog
    return None


def get_dogs(skip: int = 0, limit: int = 100) -> List[Dog]:
    return dogs_db[skip:skip + limit]


def create_dog(dog: DogCreate) -> Dog:
    db_dog = Dog(
        id=len(dogs_db) + 1,
        name=dog.name,
        breed=dog.breed,
        age=dog.age,
        created_at=datetime.now()
    )
    dogs_db.append(db_dog)
    return db_dog


def update_dog(dog_id: int, dog: DogUpdate) -> Optional[Dog]:
    for i, existing_dog in enumerate(dogs_db):
        if existing_dog.id == dog_id:
            updated_data = dog.dict(exclude_unset=True)
            dogs_db[i] = Dog(
                id=existing_dog.id,
                created_at=existing_dog.created_at,
                **updated_data
            )
            return dogs_db[i]
    return None


def delete_dog(dog_id: int) -> bool:
    global dogs_db
    original_length = len(dogs_db)
    dogs_db = [dog for dog in dogs_db if dog.id != dog_id]
    return len(dogs_db) < original_length