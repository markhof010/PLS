import csv
import os
from pathlib import Path

CSV_PATH_NAMES = str(Path(__file__).parent / 'FakeNameSet20.csv')

# A simple class to make the subscriber
class Person:
    def __init__(self, number, gender, nameSet, givenName, surname, streetAdress, zipCode, city, emailAdress, username, telephoneNumber):
        self.number = number
        self.gender = gender
        self.nameSet = nameSet
        self.givenName = givenName
        self.surname = surname
        self.streetAdress = streetAdress
        self.zipCode = zipCode
        self.city = city
        self.emailAdress = emailAdress
        self.username = username
        self.telephoneNumber = telephoneNumber

    

    def display(self):
        return ("PERSON ID: %s\nGENDER: %s\nNAMESET: %s\nGIVENNAME: %s\nSURNAME: %s\nSTREET: %s\nZIPCODE: %s\nCITY: %s\nEMAIL: %s\nUSERNAME: %s\nTELEPHONE: %s\n" % (self.number, self.gender, self.nameSet, self.givenName, self.surname, self.streetAdress, self.zipCode, self.city, self.emailAdress, self.username, self.telephoneNumber))

# A list to save the people in
class PersonList:
    def __init__(self):
        self.nameList = []
        with open(CSV_PATH_NAMES,'r', encoding='utf-8-sig') as nameCSV:
            #every row new dictionary, key and value
            reader = csv.reader(nameCSV)
            next(reader)
            for row in reader:
                self.nameList.append(Person(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))

    def addPerson(self):
        print("Add a person: ")
        #AUTO INCREMENT, LET OP +1 OF +2
        newID = len(self.nameList) + 1
        print("GENDER:")
        newGender = input()
        print("NAMESET:")
        newNameset = input()
        print("GIVENNAME:")
        newGivenname = input()
        print("SURNAME: ")
        newSurname = input()
        print("STREET:")
        newStreet = input()
        print("ZIPCODE:")
        newZipcode = input()
        print("CITY:")
        newCity= input()
        print("EMAIL:")
        newEmail = input()
        print("USERNAME:")
        newUsername = input()
        print("TELEPHONE:")
        newTelephone = str(input())

        #saving new book to the list
        self.nameList.append(Person(newID, newGender, newNameset, newGivenname, newSurname, newStreet, newZipcode, newCity, newEmail, newUsername, newTelephone))
        self._savePersons()

    def _savePersons(self):
        with open(CSV_PATH_NAMES,'w',newline='', encoding = 'utf-8-sig') as personCSV:
            fieldnames = ['Number','Gender','NameSet','GivenName','Surname','StreetAddress','ZipCode','City','EmailAddress','Username','TelephoneNumber']
            thewriter = csv.DictWriter(personCSV, fieldnames = fieldnames)
            thewriter.writeheader()
            csvList = []
            for row in self.nameList:
                rowDict = {
                    "Number": row.number,
                    "Gender": row.gender,
                    "NameSet": row.nameSet,
                    "GivenName": row.givenName,
                    "Surname": row.surname,
                    "StreetAddress": row.streetAdress,
                    "ZipCode": row.zipCode,
                    "City": row.city,
                    "EmailAddress": row.emailAdress,
                    "Username": row.username,
                    "TelephoneNumber": row.telephoneNumber
                    }
                csvList.append(rowDict)
            thewriter.writerows(csvList)