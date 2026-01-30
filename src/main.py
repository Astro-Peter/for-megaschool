# setup clean tracebacks for debugging
from rich import traceback
traceback.install()

# now import everything else
import time
import argparse
from rich import print  # print to the console with rich.print() instead of print()
from dotenv import load_dotenv, dotenv_values
import subprocess
import sys
import os

# 🚨 OPSEC ALERT 🚨 -- keep credentials SECURE in .env files!
load_dotenv()  # pull in secrets and settings
cfg = { **dotenv_values(".config") }  # pull in config settings

from modules.logger import Log  # init a logger (customize in logger.py)

######################################################## SETUP #########################################################

# CONSTANTS
GRAVITY_METRIC = 9.81  # m/s^2
GRAVITY_IMPERIAL = 32.2  # ft/s^2

# CONFIGURATION
log = Log()
start_time = time.perf_counter()  # monitor script performance

# Setup command-line arguments
parser = argparse.ArgumentParser(description='A flexible tool supporting both CLI and web API modes')
parser.add_argument('mode', nargs='?', default='cli', choices=['cli', 'api'], 
                    help='Run mode: cli for command-line interface, api for FastAPI web server')
parser.add_argument('--port', type=int, default=8000, 
                    help='Port for API mode (default: 8000)')
parser.add_argument('--host', default="127.0.0.1", 
                    help='Host for API mode (default: 127.0.0.1)')

###################################################### EXECUTION #######################################################

def main():
    args = parser.parse_args()
    
    if args.mode == 'api':
        # Run the FastAPI application via the start_api.py script
        log.hbar('Starting API Server')
        print(f'[bold blue]Starting FastAPI server on {args.host}:{args.port}[/bold blue]')
        
        # Execute the API start script with the same Python interpreter
        script_path = os.path.join(os.path.dirname(__file__), 'start_api.py')
        subprocess.run([sys.executable, script_path, '--host', args.host, '--port', str(args.port)])
    else:
        # Run the traditional CLI application
        log.hbar('Running CLI Mode')
        print('[bold magenta]Hello, world.')  # try to avoid print(), but it works with formatting too if required
        
        if testFunction():  # let's test out calling a function
            log.success('Function was called!')

        # use log.debug() when developing or debugging - not used in production
        log.debug(f'You passed in mode: [bold italic white]{args.mode}[/bold italic white]') 
        
        log.hbar(f'Inspect Object (example)')
        log.inspect(cfg)

        # log performance data
        log.info(f"Script took {time.perf_counter()-start_time:0.4f} seconds to execute.")

def testFunction():
    return True

##################################################### ENTRY POINT ######################################################

if __name__ == '__main__':
    main()  