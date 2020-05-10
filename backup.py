import json
import csv
from pathlib import Path
import os
import glob
from datetime import datetime


JSON_PATH_BOOKS = str(Path(__file__).parent / 'booksset1.json')
JSON_PATH_LOANS = str(Path(__file__).parent / 'Loans.json')
CSV_PATH_NAMES = str(Path(__file__).parent / 'FakeNameSet20.csv')
BACKUP_PATH = Path(__file__).parent / 'backups'


class Backup:
    
    def __init__(self):
        print("Making a backup")
    
    def makeBackup(self):
        with open(JSON_PATH_BOOKS,'r') as bookJson:
            allBooks = json.load(bookJson)
        with open(JSON_PATH_LOANS,'r') as loanJson:
            allLoans = json.load(loanJson)
        with open(CSV_PATH_NAMES,'r', encoding='utf-8-sig') as nameCSV:
            nameList = []
            #every row new dictionary, key and value
            for row in csv.DictReader(nameCSV):
                nameList.append(row)
        if not BACKUP_PATH.exists():
            BACKUP_PATH.mkdir()
        
        creationDate = datetime.now().strftime("%H%M%d%m%Y")
        
        backupDict = {'allBooks': allBooks, 'allLoans': allLoans, 'nameList': nameList, 'creationDate': creationDate}

        #w+: can also make a new file
        with open(str(BACKUP_PATH / f'{int(creationDate)}.json'), 'w+') as backup:
            json.dump(backupDict, backup)

class BackUpManager:
    pass

def restore():
    backups = []

    for backupsFiles in glob.glob(os.path.join(BACKUP_PATH, '*.json')):
        backups.append(backupsFiles)

    i = 1
    for backup in backups:
        print("["+ str(i) +"] " + backup)
        i = i + 1
    chose = input("Chose the number before the file you want\n")
    
    with open(backups[int(chose)-1],'r') as backupJson:
        backupFile = json.load(backupJson)
    
    with open(JSON_PATH_BOOKS,'w') as bookJson:
        json.dump(backupFile["allBooks"], bookJson)
    
    
    with open(CSV_PATH_NAMES,'w',newline='', encoding = 'utf-8-sig') as personCSV:
        fieldnames = ['Number','Gender','NameSet','GivenName','Surname','StreetAddress','ZipCode','City','EmailAddress','Username','TelephoneNumber']
        thewriter = csv.DictWriter(personCSV, fieldnames = fieldnames)
        thewriter.writeheader()
        thewriter.writerows(backupFile["nameList"])
    
restore()