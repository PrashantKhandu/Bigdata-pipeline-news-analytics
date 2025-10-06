import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from constants import *
from library.init_mongodb import get_new_mongodb_connection
from library.init_logger import get_logger


logger, mongo_client = None, None

class Processor:
    pass

class Tagger:
    pass

class TagRecords:
    pass

if __name__ == "__main__":
    logger = get_logger(NEWS)
    mongo_client = get_new_mongodb_connection()
    logger.info("Program execution started")
    logger.info("Program execution completed")
