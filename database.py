from pymongo import MongoClient
from pymongo.database import Database
from decouple import config

def client(collection)-> Database:
    client = MongoClient(f'mongodb://{config("DB_STRING")}:27017/')
    db = client[config('DB_NAME')]
    return db[f'{collection}']