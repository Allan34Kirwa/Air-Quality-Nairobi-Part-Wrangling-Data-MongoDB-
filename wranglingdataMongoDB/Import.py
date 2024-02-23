from pymongo import MongoClient
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
nairobi = db["nairobi"]

# Using the the find method to retrieve the PM 2.5 readings from site 29
result = nairobi.find(
    {"metadata.site": 29, "metadata.measurement": "P2"},
    projection = {"P2":1, "timestamp":1, "_id":0}
)
pp.pprint(result.next())