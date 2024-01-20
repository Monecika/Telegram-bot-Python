from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["TaskManager"]

Tasks = db["Tasks"]
Users = db["Users"]
