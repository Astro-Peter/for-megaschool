from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import items
from ..modules.logger import Log
import time

# Initialize the logger
log = Log()

# Create FastAPI instance
app = FastAPI(title="API Service", description="A FastAPI-based API for the application", version="1.0.0")

# Add CORS middleware (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Root endpoint that returns API information"""
    log.info("Root endpoint accessed")
    return {"message": "FastAPI API Service", "status": "running"}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": int(time.time())}

# Include the item routes
app.include_router(items.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)