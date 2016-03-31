# collborator.net
Big data project to help find users with similar interests and skills within 10 miles using MongoDB and Neo4j.

Structure of the program:

1) Querying for a specific user, attribute, organization, projects, interests, and skills will use MongoDB.
2) Querying for users with similar interests, similar skills, and organizations within 10 miles of each other will use Neo4j.

To create the database run:

"python generateDB.py users.csv organizations.csv projects.csv skills.csv interests.csv distances.csv"


