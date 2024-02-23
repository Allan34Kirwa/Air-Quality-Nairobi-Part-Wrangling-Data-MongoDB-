import pandas as pd
from pymongo import MongoClient
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=2)
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
nairobi = db["nairobi"]

# Reading records from my result into the DataFrame df
result = nairobi.find({"metadata.measurement": "P2"}).limit(3)
df = pd.DataFrame(result).set_index("timestamp")
df.head()