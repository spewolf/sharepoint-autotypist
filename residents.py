import csv

def getResident(username):
    with open('residents.csv') as residents_csv:
        reader = csv.DictReader(residents_csv)
        residents = list(reader)
    # Search
    for i in range(len(residents)):
        # List username check against username
        if getUsername(residents[i]) == username:
            return residents[i]

# Parses username from email
def getUsername(resident):
    return resident['email'].split('@')[0]