# setup clean tracebacks for debugging
from rich import traceback
traceback.install()

# now import everything else
import time
import argparse
from fastapi import FastAPI
from dotenv import load_dotenv, dotenv_values
from modules.api.endpoints import router

# 🚨 OPSEC ALERT 🚨 -- keep credentials SECURE in .env files!
load_dotenv()  # pull in secrets and settings
cfg = { **dotenv_values(".config") }  # pull in config settings

from modules.logger import Log  # init a logger (customize in logger.py)

######################################################## SETUP #########################################################

# CONFIGURATION
log = Log()
start_time = time.perf_counter()  # monitor script performance


# Initialize FastAPI app
app = FastAPI()

# Include the router from the API endpoints
app.include_router(router)

###################################################### EXECUTION #######################################################

def main():
    log.info(f"Script took {time.perf_counter()-start_time:0.4f} seconds to execute.")  # log performance data

if __name__ == '__main__':
    main()