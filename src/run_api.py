"""
Script to run the FastAPI application.
This follows the same pattern as the main.py but for the API server.
"""

# Setup clean tracebacks for debugging
from rich import traceback
traceback.install()

# Now import everything else
import time
import argparse
from rich import print
from dotenv import load_dotenv, dotenv_values

# Load environment variables
load_dotenv()
cfg = {**dotenv_values(".config")}

from src.modules.logger import Log
from src.api.main import app

######################################################## SETUP #########################################################

# Constants
DEFAULT_PORT = 8000
DEFAULT_HOST = "0.0.0.0"

# Configuration
log = Log()
start_time = time.perf_counter()

# Setup command-line arguments
parser = argparse.ArgumentParser(description='Run the FastAPI web service')
parser.add_argument('--port', type=int, default=DEFAULT_PORT, help='Port for the API server')
parser.add_argument('--host', default=DEFAULT_HOST, help='Host for the API server')
parser.add_argument('--reload', action='store_true', help='Enable auto-reload for development')

###################################################### EXECUTION #######################################################

async def run_api(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT, reload: bool = False):
    """
    Function to run the API server.
    
    Args:
        host: Host to bind the server to
        port: Port to serve the API on
        reload: Whether to enable auto-reloading during development
    """
    import uvicorn

    # Run the server
    log.info(f"Serving FastAPI application on {host}:{port}")
    if reload:
        log.warn("Development mode enabled: auto-reload is ON")
    
    config = uvicorn.Config(
        app, 
        host=host, 
        port=port, 
        reload=reload,
        log_level="info"
    )
    
    server = uvicorn.Server(config)
    await server.serve()


def main():
    """Main function to run the API server."""
    args = parser.parse_args()

    # Set up logging
    log.hbar('Starting API Server')
    log.info(f'Starting server on {args.host}:{args.port}')

    # Report which mode we're starting in
    mode = "development" if args.reload else "production" 
    log.status(f'Running in {mode} mode')

    import asyncio
    try:
        asyncio.run(run_api(args.host, args.port, args.reload))
    except KeyboardInterrupt:
        log.warn("Server shutdown requested by user")
    finally:
        log.info(f"Server shutdown complete. Script took {time.perf_counter()-start_time:0.4f} seconds to execute.")

##################################################### ENTRY POINT ######################################################

if __name__ == "__main__":
    main()