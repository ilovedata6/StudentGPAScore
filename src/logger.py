import logging
import os
from datetime import datetime

log_root_dir = os.path.join(os.getcwd(), 'Logs')
current_date = datetime.now().strftime("%Y-%m-%d")
hour = datetime.now().strftime("%H")

# Creates Logs Folder if it doesn't exist
daily_log_path = os.path.join(log_root_dir, current_date)
os.makedirs(daily_log_path, exist_ok=True)

# Log file name based on the current hour and date
log_file = f"{hour}_{current_date}.log"
log_file_path = os.path.join(daily_log_path, log_file)

# Logging Configuration
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


logger = logging.getLogger(__name__)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)