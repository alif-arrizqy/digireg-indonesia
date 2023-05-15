from pymongo import MongoClient

def mongo_connection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["digireg"]
    collection = db["todo_list"]
    return collection