from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import time


class HealthCheck(BaseModel):
    status: str
    uptime: float
    version: str


class APIResponse(BaseModel):
    message: str
    data: Optional[dict] = None


class CalculationRequest(BaseModel):
    value: float
    unit: str = "metric"  # default to metric system


class CalculationResponse(APIResponse):
    result: float


# Initialize the FastAPI app
app = FastAPI(
    title="Project API",
    description="A FastAPI API service for calculations and utilities",
    version="1.0.0"
)


@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the project API!", "project": "FastAPI implementation"}


@app.get("/health", response_model=HealthCheck)
async def health_check():
    """
    Health check endpoint that returns the status of the API.
    """
    start_time = time.time()  # In a real implementation, this would be tracked since startup
    return {
        "status": "healthy",
        "uptime": start_time,
        "version": "1.0.0"
    }


@app.get("/api/v1/status", response_model=APIResponse)
async def get_status():
    """
    Example API endpoint v1 that returns API status.
    """
    return APIResponse(message="API is running", data={"status": "active"})


@app.post("/api/v1/process", response_model=APIResponse)
async def process_data(request: APIResponse):
    """
    Example POST endpoint that echoes back the received data.
    """
    return APIResponse(message="Data processed successfully", data=request.dict())


# Using constants from the main.py for demonstration 
GRAVITY_METRIC = 9.81  # m/s^2
GRAVITY_IMPERIAL = 32.2  # ft/s^2


@app.post("/api/v1/calculate/gravity", response_model=CalculationResponse)
async def calculate_gravity_force(request: CalculationRequest):
    """
    Calculate force based on mass and gravitational constant.
    For demonstration purposes, assume mass = value input provided.
    """
    gravity_constant = GRAVITY_METRIC if request.unit == "metric" else GRAVITY_IMPERIAL
    force = request.value * gravity_constant  # F = m * g
    
    return CalculationResponse(
        message=f"Calculated force using {request.unit} units",
        data={"mass": request.value, "gravity": gravity_constant},
        result=force
    )


@app.get("/api/v1/calculate/earth-gravity/{mass}", response_model=CalculationResponse)
async def get_earth_gravity_force(mass: float):
    """
    Calculate force based on mass using Earth's gravitational constant (metric).
    Path param based endpoint for simpler calculation.
    """
    gravity_constant = GRAVITY_METRIC
    force = mass * gravity_constant  # F = m * g
    
    return CalculationResponse(
        message=f"Earth gravity force calculated for mass {mass}",
        data={"mass": mass, "gravity": gravity_constant},
        result=force
    )