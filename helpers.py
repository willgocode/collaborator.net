import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

def storeUsers(filename, db):
    "This reads users.csv and generates a collection for it."
    csvfile = open(filename, 'r')
    splitString = filename.split( '.csv')
    collection = db.Users
    data = pd.read_csv(csvfile)
    data_json = json.loads(data.to_json(orient = 'records'))
    collection.remove()
    collection.insert(data_json)

    return

def storeDistances(filename, db):
	"This reads the distance.csv and generates a collection for it."
	csvfile = open(filename, 'r')
	splitString = filename.split( '.csv')
	collection = db.Distances
	data = pd.read_csv(csvfile)
	data_json = json.loads(data.to_json(orient = 'records'))
	collection.remove()
	collection.insert(data_json)

	return

def updateOrganization(filename, db):
    "This updates a user with a new organization field."
    csvfile = open(filename, 'r')
    splitString = filename.split('.csv')

    data = pd.read_csv(csvfile)
    data_json = json.loads(data.to_json(orient = 'records'))

    for row in data_json:
        write_result = db.Users.update(
            {'user_id' : row["user_id"]},
            {
                '$set':{
                    "organization" : row["organization"]
                },
            }
        )

    return

def updateProjects(filename, db):
    "This updates a user with new a new projects field."
    csvfile = open(filename, 'r')
    splitString = filename.split('.csv')

    data = pd.read_csv(csvfile)
    data_json = json.loads(data.to_json(orient = 'records'))

    for row in data_json:
        write_result = db.Users.update(
            {'user_id' : row["user_id"]},
            {
                '$set':{
                    "project" : row["project"]
                },
            }
        )

    return

def updateSkills(filename, db):
    "This updates a user with a new skills field."
    csvfile = open(filename, 'r')
    splitString = filename.split('.csv')

    data = pd.read_csv(csvfile)
    data_json = json.loads(data.to_json(orient = 'records'))

    for row in data_json:
        write_result = db.Users.update(
            {'user_id' : row["user_id"]},
            {
                '$set':{
                    "skill" : row["skill"],
					"skill_level" : row["skill_level"]
                },
            }
        )

    return

def updateInterests(filename, db):
    "This updates a user with a new interests field."
    csvfile = open(filename, 'r')
    splitString = filename.split('.csv')

    data = pd.read_csv(csvfile)
    data_json = json.loads(data.to_json(orient = 'records'))

    for row in data_json:
        write_result = db.Users.update(
            {'user_id' : row["user_id"]},
            {
                '$set':{
                    "interest" : row["interest"],
					"interest_level" : row["interest_level"]
                },
            }
        )

    return
