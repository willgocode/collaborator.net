import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

csvfile = open('test.csv', 'r')
client = MongoClient('localhost', 27017)
db = client['test-database']
collection_name = 'test_collection'
collection = db.collection_name
data = pd.read_csv(csvfile)
data_json = json.loads(data.to_json(orient = 'records'))
collection.remove()
collection.insert(data_json)

cursor = db.collection_name.find()

for document in cursor:
	print(document)
