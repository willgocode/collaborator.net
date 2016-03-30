import csv
import json
import pandas as pd
import sys, getopt, pprint
import helpers
from pymongo import MongoClient 

def main(argv): 
	usersFile = ''
	organizationsFile = ''
	projectFile = ''
	skillsFile = ''
	interestsFile = ''
	distancesFile = ''

	if len(argv) == 0:
		print 'Error: Not enough arguments. Type "python generateDB.py -h" for help.'
		sys.exit()
	
	client = MongoClient('localhost', 27017)
	db = client['collaboratornet']	

	try:
		opts, args = getopt.getopt(argv, "h", ["users="])
#, "organizations=", "projects=", 
#						"skills=", "interests=", "distances="])
	except getopt.GetoptError:
		sys.exit()
	
	for opt, arg in opts:
		if opt == '-h':
			print 'Run program with "python generateDB.py <users>.csv <organizations>.csv <projects>.csv <skills>.csv <interests>.csv <distances>.csv".'
			sys.exit()

	print('Reading: users')
	usersFile = sys.argv[1]
	helpers.storeFile(usersFile, db)

#	print('Reading: organizations')
#	helpers.updateOrganization('organizations.csv', db)

#	print('Reading: projects')

#	print('Reading: skills')

#	print('Reading: interests')

#	print('Reading: distances')

if __name__ == "__main__":
	main(sys.argv[1:])
