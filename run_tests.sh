#!/bin/bash

echo "Running API tests..."

# Install dependencies if not already installed
pip install -r requirements.txt

# Run pytest to test the API
python -m pytest test/test_api.py -v