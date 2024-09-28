import logging
import os
from datetime import datetime

log_root_dir = os.path.join(os.getcwd(), 'logs')
current_date = datetime.now().strftime("%Y-%m-%d")
hour = datetime.now().strftime("%H")  

# Create the log directory if it doesn't exist
daily_log_path = os.path.join(log_root_dir, current_date)
os.makedirs(daily_log_path, exist_ok=True)

# Log file name based on the current hour
log_file = f"{hour}.log"
log_file_path = os.path.join(daily_log_path, log_file)

# Set up the logging configuration
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Create a logger
logger = logging.getLogger(__name__)

# Add handlers for each log level if needed (optional, for more control over warning/error logs)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # This will print to console for immediate feedback
formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)