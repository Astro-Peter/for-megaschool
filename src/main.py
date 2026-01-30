# setup clean tracebacks for debugging
from rich import traceback
traceback.install()

# now import everything else
import time
import argparse
from rich import print  # print to the console with rich.print() instead of print()
from dotenv import load_dotenv, dotenv_values
from fastapi import FastAPI
from src.api.routes import router

# 🚨 OPSEC ALERT 🚨 -- keep credentials SECURE in .env files!
load_dotenv()  # pull in secrets and settings
cfg = { **dotenv_values(".config") }  # pull in config settings

from modules.logger import Log  # init a logger (customize in logger.py)

######################################################## SETUP #########################################################

# CONSTANTS
GRAVITY_METRIC = 9.81  # m/s^2
GRAVITY_IMPERIAL = 32.2  # ft/s^2

# CONFIGURATION
app = FastAPI()
log = Log()
start_time = time.perf_counter()  # monitor script performance

# Include the routes
app.include_router(router)

###################################################### EXECUTION #######################################################

@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    log.info(f"Script took {time.perf_counter()-start_time:0.4f} seconds to execute.")  # log performance data