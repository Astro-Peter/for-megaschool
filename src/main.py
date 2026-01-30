# setup clean tracebacks for debugging
from rich import traceback
traceback.install()

# now import everything else
import time
import argparse
from rich import print  # print to the console with rich.print() instead of print()
from dotenv import load_dotenv, dotenv_values

# 🚨 OPSEC ALERT 🚨 -- keep credentials SECURE in .env files!
load_dotenv()  # pull in secrets and settings
cfg = { **dotenv_values(".config") }  # pull in config settings

from modules.logger import Log  # init a logger (customize in logger.py)

# API functionality import
try:
    from src.api.server import run_server  # Import the API server function
except ImportError:
    run_server = None  # In case API dependencies aren't installed

######################################################## SETUP #########################################################

# CONSTANTS
GRAVITY_METRIC = 9.81  # m/s^2
GRAVITY_IMPERIAL = 32.2  # ft/s^2

# CONFIGURATION
log = Log()
start_time = time.perf_counter()  # monitor script performance

# setup any command-line arguments we need
parser = argparse.ArgumentParser(description='Python Project Template - CLI tool and API server')
parser.add_argument('argname', nargs='?', help='A sample argument for CLI mode (optional)')   # define arguments like this
parser.add_argument('--serve-api', action='store_true', help='Run the FastAPI server instead of normal execution')
parser.add_argument('--host', default='127.0.0.1', help='Host address for the API server (default: 127.0.0.1)')
parser.add_argument('--port', type=int, default=8000, help='Port for the API server (default: 8000)')
parser.add_argument('--reload', action='store_true', help='Enable auto-reload for API development')


###################################################### EXECUTION #######################################################

def main():
    """Add functionality for your script here."""
    
    args = parser.parse_args()  # pull in command-line arguments
    
    # Check if API server is requested
    if args.serve_api:
        if run_server is None:
            log.danger("API dependencies not available. Please install requirements: pip install -r requirements.txt")
            return
        
        log.status(f'Starting FastAPI server on {args.host}:{args.port}')
        run_server(host=args.host, port=args.port, reload=args.reload)
        return  # Exit after starting the server
    
    # Otherwise, run normal CLI behavior
    # report the results
    log.hbar('Results')
    print('[bold magenta]Hello, world.')  # try to avoid print(), but it works with formatting too if required
    
    if testFunction():  # let's test out calling a function
        log.success('Function was called!')

    # use log.debug() when developing or debugging - not used in production
    if args.argname:  # Only log if an argument was provided
        log.debug(f'You passed in this argument: [bold italic white]{args.argname}[/bold italic white]') 
    
    # log.inspect() is also useful for debugging
    log.hbar(f'Inspect Object (example)')
    log.inspect(cfg)


def testFunction():
    return True


##################################################### ENTRY POINT ######################################################

if __name__ == '__main__':
    main()  
    log.info(f"Script took {time.perf_counter()-start_time:0.4f} seconds to execute.")  # log performance data