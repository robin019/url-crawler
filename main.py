from app.datasource import DataSource
from app.logger import logger

if __name__ == '__main__':
    logger.info("start updating database")
    for source in DataSource.get_datasource():
        source.execute()
    logger.info("successfully update database")