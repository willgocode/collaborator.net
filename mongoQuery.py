import sys, getopt
from pymongo import MongoClient

def main(argv):
	fileList = [ '', '', '', '']
	query = {}
	userName = ''
#	organizationName = ''
#	projectName = ''
#	interestName = ''
#	skillName = ''

	client = MongoClient('localhost', 27017)
	db = client['collaboratornet']
	collection = db['Users']

	if len(argv) == 0:
		print ('Finding all users in database: \n')
		users = collection.find()
		for i in users:
			print i
			print '\n' 
	try:
		opts, args = getopt.getopt(argv, "hu:o:p:i:s:",["userName=", "organizationName=", 
					"projectName=", "interestName=", "skillList="])

	except getopt.GetoptError:
		print 'See "python mongoQuery.py -h" for help on running program.'
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print 'Enter parameters to query for: \n'
			print '-u = query for user \n'
			print '-o = query for organization \n'
			print '-p = query for project \n'
			print '-i = query for interest \n'
			print '-s = query for skill \n'
			print 'You may use any combination of these.\n'
			print 'Example:\n'
			print 'python mongoQuery -u <userName> -o <organizationName> \n'
			print 'will find all users of that name in that organization.\n'
			sys.exit()

		elif opt in ("-u", "--userName"):
			userName = arg.split()
			query['first_name'] = userName[0]
			query['last_name'] = userName[1]
		elif opt in ("-o", "--organizationName"):
			fileList[0] = arg
			query['organization'] = fileList[0]
		elif opt in ("-p", "--projectName"):
			fileList[1] = arg
			query['project'] = fileList[1]
		elif opt in ("-i", "--interestName"):
			fileList[2] = arg
			query['interest'] = fileList[2]
		elif opt in ("-s", "skillName"):
			fileList[3] = arg
			query['skill'] = fileList[3]

	cursor = collection.find( query )
	for i in cursor:
		print i
	
if __name__ == "__main__":
	main(sys.argv[1:])
