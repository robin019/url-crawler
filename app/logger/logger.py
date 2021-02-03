import logging
from settings import config

LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, filename=config.LOG_FILE, format=LOGGING_FORMAT, datefmt=DATE_FORMAT)