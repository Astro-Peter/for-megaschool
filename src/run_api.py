"""
API Server Entry Point
Use this file to start the FastAPI server.
Example usage:
    python -m src.run_api
Or:
    uvicorn src.run_api:app --reload
"""

# Setup clean tracebacks for debugging
from rich import traceback
traceback.install()

# Import everything else
import argparse
from rich import print  # print to the console with rich.print() instead of print()
from dotenv import load_dotenv, dotenv_values

# 🚨 OPSEC ALERT 🚨 -- keep credentials SECURE in .env files!
load_dotenv()  # pull in secrets and settings
cfg = { **dotenv_values(".config") }  # pull in config settings

from modules.logger import Log  # init a logger (customize in logger.py)
from modules.api import app  # import the FastAPI app

# Configuration
log = Log()


def serve_api(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """Start the API server."""
    import uvicorn
    log.info(f"Starting API server on {host}:{port}")
    
    uvicorn.run(
        "src.modules.api:app",
        host=host,
        port=port,
        reload=reload,
        log_level="info"
    )


def main():
    """Entry point for API server with command-line arguments."""
    parser = argparse.ArgumentParser(description='Run the FastAPI server')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host for the API server (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=8000, help='Port for the API server (default: 8000)')
    parser.add_argument('--reload', action='store_true', help='Enable auto-reload on code changes')
    
    args = parser.parse_args()

    # Initialize configuration settings
    cfg = {**dotenv_values(".config")}
    
    # Start the API server
    serve_api(host=args.host, port=args.port, reload=args.reload)


if __name__ == "__main__":
    main()