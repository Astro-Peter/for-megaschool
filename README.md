# FastAPI User API

## Overview
This FastAPI application allows handling user requests and responses via HTTP endpoints.

## Endpoints
- **POST /users/**: Create a new user
- **GET /users/{user_id}**: Retrieve a user by ID

## Requirements
- fastapi
- python-dotenv
- rich

## Running the Application
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `uvicorn src.main:app --reload`
