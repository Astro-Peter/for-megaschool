from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Here you can define more routes and corresponding endpoints.



@app.post("/items/")
from src.models import Item


async def create_item(item: Item):
    return item


from starlette.responses import PlainTextResponse
from middleware import CustomErrorMiddleware
app.add_middleware(CustomErrorMiddleware)
