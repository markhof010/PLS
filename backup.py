import json
import csv
from pathlib import Path
import os
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
        with open(CSV_PATH_NAMES,'r') as nameCSV:
            nameList = []
            #every row new dictionary, key and value
            for row in csv.DictReader(nameCSV, skipinitialspace=True):
                nameList.append(row)
        if not BACKUP_PATH.exists():
            BACKUP_PATH.mkdir()
        
        creationDate = datetime.now().timestamp()
        
        backupDict = {'allBooks': allBooks, 'allLoans': allLoans, 'nameList': nameList, 'creationDate': creationDate}

        #w+: can also make a new file
        with open(str(BACKUP_PATH / f'{int(creationDate)}.json'), 'w+') as backup:
            json.dump(backupDict, backup)

class BackUpManager:
    pass