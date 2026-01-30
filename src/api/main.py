from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import router as api_router

app = FastAPI(
    title="FastAPI Service",
    description="A FastAPI-based API service",
    version="0.1.0",
)

# Add CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "FastAPI service is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)