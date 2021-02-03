import logging as logger
from settings import config

LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
logger.basicConfig(level=logger.INFO, filename=config.LOG_FILE, format=LOGGING_FORMAT, datefmt=DATE_FORMAT)