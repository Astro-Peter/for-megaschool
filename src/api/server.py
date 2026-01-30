"""
API Server Module
This module contains logic to launch the FastAPI application server.
"""

import uvicorn
import argparse
from .fastapi_app import app


def run_server(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """
    Run the FastAPI server with specified configuration.
    
    Args:
        host (str): Host address to bind to
        port (int): Port number to listen on
        reload (bool): Enable auto-reload on code changes (development mode)
    """
    uvicorn.run(
        "src.api.fastapi_app:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Launch FastAPI server')
    parser.add_argument('--host', default='127.0.0.1', 
                        help='Host address to bind to (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=8000, 
                        help='Port number to listen on (default: 8000)')
    parser.add_argument('--reload', action='store_true', 
                        help='Enable auto-reload on code changes (development mode)')
    
    args = parser.parse_args()
    
    run_server(host=args.host, port=args.port, reload=args.reload)