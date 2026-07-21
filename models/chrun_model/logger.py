import os
import logging

# Import configuration
from config.config import LOG_DIR

# Create logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Log file path
LOG_FILE = os.path.join(LOG_DIR, "api.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Logger instance
logger = logging.getLogger(__name__)