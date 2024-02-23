from pymongo import MongoClient
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
nairobi = db["nairobi"]

# Using  find method to retrieve the PM 2.5 readings from all sites
result = nairobi.find({"metadata.measurement": "P2"}).limit(3)
pp.pprint(list(result))