from fastapi import APIRouter
from models.item import Item

router = APIRouter()

@router.post("/items/")
async def create_item(item: Item):
    return item

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}
from sqlalchemy.orm import Session
from database import SessionLocal

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/")
async def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = DBItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items/{item_id}")
async def read_item(item_id: int, db: Session = Depends(get_db)):
    return db.query(DBItem).filter(DBItem.id == item_id).first()