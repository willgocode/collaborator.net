import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

print('Storing users')
csvfile = open('users.csv', 'r')
client = MongoClient('localhost', 27017)
db = client['collaboratornet']
collection = db.Users
data = pd.read_csv(csvfile)
data_json = json.loads(data.to_json(orient = 'records'))
collection.remove()
collection.insert(data_json)

print('Reading: organizations')

print('Reading: projects')

print('Reading: skills')

print('Reading: interests')

print('Reading: distances')
