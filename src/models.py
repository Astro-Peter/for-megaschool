from pydantic import BaseModel

# Example request and response models can be defined here.
class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True
