import csv
import json
import pandas as pd
import sys, getopt, pprint
import helpers
from pymongo import MongoClient 
 
client = MongoClient('localhost', 27017)
db = client['collaboratornet']

print('Reading: users')
helpers.storeFile('users.csv', db)

print('Reading: organizations')
helpers.updateOrganization('organizations.csv', db)

print('Reading: projects')

print('Reading: skills')

print('Reading: interests')

print('Reading: distances')
