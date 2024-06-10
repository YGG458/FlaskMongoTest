from pymongo import MongoClient
import os
from werkzeug.local import LocalProxy
def get_client():
    connect_string = os.getenv('MONGODB_URI')
    if not connect_string:
        raise ValueError("Environment variable MONGODB_URI is not set.")
    return MongoClient(connect_string)

def get_database():
    client=get_client()
    db=client['Abandon']
    return db

def get_collection(database_name,collction_name):
    return database_name[collction_name]

db = LocalProxy(get_database)

