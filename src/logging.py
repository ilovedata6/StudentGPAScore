import logging
import os 
from datetime import datetime

LOGFILE = f"{datetime.now().strftime("%d_%m_%Y_%H_%M_%S").log}"
logs_path = os.path.join(os.getcwd(),LOGFILE)
os.makedirs(logs_path,exist_ok=True)

LOGFILE_PATH = os.path.join(logs_path,LOGFILE)

logging.basicConfig(
    filename = LOGFILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name) - %(levelname)s - %(message)s",
    level=logging.INFO,
)

