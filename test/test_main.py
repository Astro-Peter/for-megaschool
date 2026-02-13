import pytest
from httpx import AsyncClient
from src.main import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI application!"}

@pytest.mark.asyncio
async def test_create_item():
    item_data = {"name": "item1", "price": 100}
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"item": item_data}