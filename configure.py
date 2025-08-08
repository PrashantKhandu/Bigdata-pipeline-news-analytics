import pymongo
from constants import *

mongo_client = pymongo.MongoClient("localhost", 27017)

### Index creation on DB-Collections
print("News DB index creation started")
mongo_client[NEWS][NEWS].create_index([("url", pymongo.ASCENDING)], unique=True)
mongo_client[NEWS][NEWS].create_index([("website", pymongo.ASCENDING)])
mongo_client[NEWS][NEWS].create_index([("date_added", pymongo.ASCENDING)])
mongo_client[NEWS][NEWS].create_index([("last_updated", pymongo.ASCENDING)])
mongo_client[NEWS][URLS].create_index([("url", pymongo.ASCENDING)], unique=True)
mongo_client[NEWS][URLS].create_index([("scrape_status", pymongo.ASCENDING)], unique=True)
mongo_client[NEWS][WEBSITES].create_index([("website", pymongo.ASCENDING)], unique=True)
print("News DB index created")

print("Keywords DB index creation started")
mongo_client[KEYWORDS][KEYWORDS].create_index([{"keyword", pymongo.DESCENDING}], unique=True)
mongo_client[KEYWORDS][PLACES].create_index([{"place_name", pymongo.DESCENDING}], unique=True)
print("Keywords DB index created")
