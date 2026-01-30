from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def read_health():
    return {"status": "healthy"}

@router.get("/message")
def read_message():
    return {"message": "Hello from FastAPI!"}