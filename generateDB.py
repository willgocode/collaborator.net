import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
 
def storeFile(filename):
	"This reads a file and generates a collection for it."
	csvfile = open(filename, 'r')
	splitString = filename.split( '.csv')
	collection = db[splitString[0]]
	data = pd.read_csv(csvfile)
	data_json = json.loads(data.to_json(orient = 'records'))
	collection.remove()
	collection.insert(data_json)
	return

client = MongoClient('localhost', 27017)
db = client['collaboratornet']

print('Reading: users')
storeFile('users.csv')

print('Reading: organizations')
#storeFile('organizations.csv')

print('Reading: projects')

print('Reading: skills')

print('Reading: interests')

print('Reading: distances')
