from pymongo.errors import ConnectionFailure
import configparser
import traceback
import pymongo
import os, sys

PROJECT_FOLDER_LOCATION = os.getenv("PROJECT_FOLDER_LOCATION")
sys.path.append(PROJECT_FOLDER_LOCATION)
from library.init_logger import get_logger

g_mongo_client = None


def get_configurations():
    logger = get_logger()
    CONFIG_FILE = os.path.join(PROJECT_FOLDER_LOCATION, "config.ini")
    if not os.path.exists(CONFIG_FILE):
        logger.critical(f"config.ini file doesn't exist in {CONFIG_FILE}")
        exit()
    cfg = configparser.ConfigParser()
    cfg.read(CONFIG_FILE)
    hostname = cfg["MONGODB"]["address"]
    port = cfg["MONGODB"]["port"]
    return hostname, port


def _check_shared_mongodb_connection():
    global g_mongo_client
    if g_mongo_client == None:
        return False
    try:
        g_mongo_client.admin.command("ping")
    except:
        g_mongo_client = None
        return False
    return True


def get_shared_mongodb_connection():
    global g_mongo_client
    if _check_shared_mongodb_connection():
        return g_mongo_client
    logger = get_logger()
    try:
        hostname, port = get_configurations()
        g_mongo_client = pymongo.MongoClient(hostname, int(port))
        info = g_mongo_client.server_info()
        logger.debug("Server Info : {}".format(info))
        logger.debug("MongoDB is Active")
        logger.debug("Connection created to MongoDB Database.")
        return g_mongo_client
    except [ConnectionFailure, Exception]:
        logger.critical("MongoDB is Inactive. Exiting")
        logger.critical("{}".format(traceback.format_exc()))
        exit()


def close_shared_mongodb_connection():
    global g_mongo_client
    if _check_shared_mongodb_connection():
        g_mongo_client.close()
    g_mongo_client = None


def get_new_mongodb_connection():
    logger = get_logger()
    try:
        hostname, port = get_configurations()
        mongo_client = pymongo.MongoClient(hostname, int(port))
        info = mongo_client.server_info()
        logger.debug("Server Info : {}".format(info))
        logger.debug("MongoDB is Active")
        logger.debug("Connection created to MongoDB Database.")
        return mongo_client
    except [ConnectionFailure, Exception]:
        logger.critical("MongoDB is Inactive. Exiting")
        logger.critical("{}".format(traceback.format_exc()))
        exit()
