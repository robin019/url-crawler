import psycopg2
from settings import config
from app.logger import logger

# Database
try:
    connection = psycopg2.connect(user=config.DATABASE_USER,
                                  password=config.DATABASE_PASSWORD,
                                  host=config.DATABASE_HOST,
                                  port=config.DATABASE_PORT,
                                  database=config.DATABASE_NAME)
except:
    logger.error('Catch an exception.', exc_info=True)
