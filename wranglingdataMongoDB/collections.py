from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
for c in db.list_collections():
    print(c["name"])