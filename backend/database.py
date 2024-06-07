from pymongo import MongoClient

def get_client():
    connect_string = 'mongodb+srv://guan:Aa123456@abandon.wga0hxr.mongodb.net/?retryWrites=true&w=majority&appName=Abandon'
    return MongoClient(connect_string)

def get_database(client):
    return client['Abandon']

def get_collection(database_name,collction_name):
    return database_name[collction_name]



