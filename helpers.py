import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

def storeFile(filename, db):
    "This reads a file and generates a collection for it."
    csvfile = open(filename, 'r')
    splitString = filename.split( '.csv')
    collection = db[splitString[0]]
    data = pd.read_csv(csvfile)
    data_json = json.loads(data.to_json(orient = 'records'))
    collection.remove()
    collection.insert(data_json)

    return

def updateOrganization(filename, db):
    "This updates a user with new fields."
    csvfile = open(filename, 'r')
    splitString = filename.split('.csv')

    data = pd.read_csv(csvfile)
    data_json = json.loads(data.to_json(orient = 'records'))

    for row in data_json:
        write_result = db.users.update(
            {'user_id' : row["user_id"]},
            {
                '$set':{
                    "organization" : row["organization"]
                },
            }
        )

    return


