#!/bin/bash

echo "Starting FastAPI server..."
pip install -r requirements.txt
python -m uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000