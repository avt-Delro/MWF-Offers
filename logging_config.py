import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pathlib import Path

logger = logging.getLogger("mwf")
log_file = Path(f"logs/MWF_Update{datetime.now().strftime('%Y%m%d')}.log")

# Streamlit can re-run/reload modules. Rebuild this logger's handlers so one
# log event is written once, even after repeated imports.
for existing_handler in logger.handlers[:]:
    logger.removeHandler(existing_handler)
    existing_handler.close()

handler = RotatingFileHandler(
    log_file,
    maxBytes=10_000_000,
    backupCount=3
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.setLevel(logging.INFO)
logger.propagate = False
