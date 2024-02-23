from pymongo import MongoClient
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
nairobi = db["nairobi"]

# Count the number of documents
nairobi.count_documents({})

# Retrive one document
result = nairobi.find_one({})
pp.pprint(result)

# Using distinct
nairobi.distinct("metadata.site")

# Distinct type of measurements
nairobi.distinct("metadata.measurement")

# nairobi.count_documents({"metadata.site":6})
print("Documents from site 6:", nairobi.count_documents({"metadata.site":6}))
print("Documents from site 29:", nairobi.count_documents({"metadata.site":29}))