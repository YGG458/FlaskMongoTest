from pymongo import MongoClient
import os

def get_client():
    connect_string = os.getenv('MONGODB_URI')
    if not connect_string:
        raise ValueError("Environment variable MONGODB_URI is not set.")
    return MongoClient(connect_string)

def get_database(client):
    return client['Abandon']

def get_collection(database_name,collction_name):
    return database_name[collction_name]

