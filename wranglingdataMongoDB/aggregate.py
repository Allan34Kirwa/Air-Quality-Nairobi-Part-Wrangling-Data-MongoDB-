
from pymongo import MongoClient
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
nairobi = db["nairobi"]

# Using aggregate to retrieve the PM 2.5 readings from all sites
result = nairobi.aggregate(
    [
        {"$group":{"_id": "$metadata.site", "count": {"$count": {}}}}
    ]
)
pp.pprint(list(result))

# Number of readings there are for each type ("humidity", "temperature", "P2", and "P1") in site 6.

result = nairobi.aggregate(
    [
        {"$match": {"metadata.site":6}},
        {"$group":{"_id": "$metadata.measurement", "count": {"$count": {}}}}
    ]
)
pp.pprint(list(result))