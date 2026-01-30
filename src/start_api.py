#!/usr/bin/env python3
"""
Standalone script to start the FastAPI server
"""
import sys
import os
import argparse
from modules.logger import Log

# Add src to path to allow imports from same directory level
sys.path.append(os.path.dirname(__file__))

def main():
    parser = argparse.ArgumentParser(description='Start the FastAPI API server')
    parser.add_argument('--port', type=int, default=8000, 
                        help='Port for API mode (default: 8000)')
    parser.add_argument('--host', default="127.0.0.1", 
                        help='Host for API mode (default: 127.0.0.1)')
    
    args = parser.parse_args()
    
    log = Log()
    log.hbar('Starting API Server')
    log.info(f'Starting FastAPI server on {args.host}:{args.port}')
    
    # Now we can import the API components
    from api.main import app
    import uvicorn
    
    # Use uvicorn to run the FastAPI app
    uvicorn.run(
        app, 
        host=args.host, 
        port=args.port,
        reload=False,  # Set to True for development
        log_level="info"
    )

if __name__ == "__main__":
    main()