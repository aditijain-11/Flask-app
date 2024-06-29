from pymongo import MongoClient
from flask import json
with open('../config.json') as config_file:
    config = json.load(config_file)
client = MongoClient(config.get("MONGODB_URI"))
db = client['user_db']
collection = db['user_info']

# class DbMethods:
#     @classmethod
#     async def create_record(cls,data:dict):
#         try:
#             collection.insert_one(data)
#         except Exception as e:
#             raise