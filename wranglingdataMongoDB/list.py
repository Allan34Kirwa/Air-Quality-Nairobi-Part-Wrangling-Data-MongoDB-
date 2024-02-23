from pprint import PrettyPrinter
from pymongo import MongoClient
pp = PrettyPrinter(indent=2)
client = MongoClient(host="localhost", port=27017)
pp.pprint(list(client.list_databases()))
