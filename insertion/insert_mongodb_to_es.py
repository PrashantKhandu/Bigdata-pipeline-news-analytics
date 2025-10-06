import traceback
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from constants import *
from library.init_mongodb import get_new_mongodb_connection
from library.init_logger import get_logger


logger, mongo_client = None, None


def validate_mongodb_records(limit:int=1000):
    pass

def insert_to_elastic_search(records:dict):
    pass

def main():
    records = dict()
    try:
        records = validate_mongodb_records()
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())
    if not len(records):
        logger.critical(f"Got {len(records)} records. Exiting...")
        exit()
    try:
        insert_to_elastic_search(records=records)
    except Exception as e:
        logger.error(e)
        logger.error(traceback.format_exc())


if __name__ == "__main__":
    logger = get_logger(INSERTION)
    mongo_client = get_new_mongodb_connection()
    logger.info("Program execution started")
    logger.info("Program execution completed")
