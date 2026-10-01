from pymongo import MongoClient

from app.core.config import settings


def get_observations_collection():
    client = MongoClient(settings.mongo_url, serverSelectionTimeoutMS=3000)
    return client[settings.mongo_database]["observations"]