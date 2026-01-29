# setup clean tracebacks for debugging
from rich import traceback
traceback.install()

# now import everything else
import time
import argparse
import sys
from rich import print  # print to the console with rich.print() instead of print()
from dotenv import load_dotenv, dotenv_values

# 🚨 OPSEC ALERT 🚨 -- keep credentials SECURE in .env files!
load_dotenv()  # pull in secrets and settings
cfg = { **dotenv_values(".config") }  # pull in config settings

from modules.logger import Log  # init a logger (customize in logger.py)
from modules.app import app  # FastAPI application

######################################################## SETUP #########################################################

# CONSTANTS
GRAVITY_METRIC = 9.81  # m/s^2
GRAVITY_IMPERIAL = 32.2  # ft/s^2

# CONFIGURATION
log = Log()
start_time = time.perf_counter()  # monitor script performance

# setup any command-line arguments we need
parser = argparse.ArgumentParser(description='FastAPI application with health check endpoint')
parser.add_argument('--mode', default='cli', choices=['cli', 'server'], 
                    help='Run mode: cli for command line, server for FastAPI server')
parser.add_argument('--host', default='127.0.0.1', help='Server host address')
parser.add_argument('--port', type=int, default=8000, help='Server port number')
parser.add_argument('argname', nargs='?', help='<describe the arg here>')   # define arguments like this


###################################################### EXECUTION #######################################################

def main():
    """Add functionality for your script here."""
    
    args = parser.parse_args()  # pull in command-line arguments

    if args.mode == 'server':
        runFastAPIServer(args.host, args.port)
    else:
        runCLI(args)


def runCLI(args):
    """Run the application in CLI mode."""
    # report the results
    log.hbar('Results')
    print('[bold magenta]Hello, world.')  # try to avoid print(), but it works with formatting too if required
    
    if testFunction():  # let's test out calling a function
        log.success('Function was called!')

    # use log.debug() when developing or debugging - not used in production
    if args.argname:
        log.debug(f'You passed in this argument: [bold italic white]{args.argname}[/bold italic white]') 
    
    # log.inspect() is also useful for debugging
    log.hbar(f'Inspect Object (example)')
    log.inspect(cfg)


def runFastAPIServer(host: str = '127.0.0.1', port: int = 8000):
    """
    Run the FastAPI server.
    
    Args:
        host: Server host address
        port: Server port number
    """
    import uvicorn
    
    log.hbar('Starting FastAPI Server')
    log.info(f'Starting server on [bold]{host}[/bold]:[bold]{port}[/bold]')
    log.info('Visit [bold underline]http://{0}:{1}/docs[/bold underline] for interactive API documentation'.format(host, port))
    log.info('Visit [bold underline]http://{0}:{1}/health[/bold underline] for health check'.format(host, port))
    
    try:
        uvicorn.run(
            "modules.app:app",
            host=host,
            port=port,
            reload=False,
            log_level="info"
        )
    except KeyboardInterrupt:
        log.info('Server shutdown requested.')
    except Exception as e:
        log.danger(f'Server error: {e}')
        sys.exit(1)


def testFunction():
    return True


##################################################### ENTRY POINT ######################################################

if __name__ == '__main__':
    main()  
    if '--mode' not in sys.argv or sys.argv[sys.argv.index('--mode') + 1] == 'cli':
        log.info(f"Script took {time.perf_counter()-start_time:0.4f} seconds to execute.")  # log performance data
