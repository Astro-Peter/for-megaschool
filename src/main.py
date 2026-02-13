from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def read_health():
    return {"status": "OK"}
from fastapi import FastAPI
from routers.items import router as items_router

app = FastAPI()

# Include the items router
app.include_router(items_router)

@app.get("/health")
def read_health():
    return {"status": "OK"}
