import books
import person
import os
import json
from pathlib import Path

JSON_PATH = str(Path(__file__).parent / 'loan.json')

class Loan:
    
    def __init__(self, book, person):
        self.person = person
        self.book = book
    
    def toDict(self):
        return {'person': {'Number': self.person.number,'Gender': self.person.gender, 'NameSet': self.person.nameSet,'GivenName': self.person.givenName,'Surname': self.person.surname,'StreetAddress': self.person.streetAdress,'ZipCode': self.person.zipCode,'City': self.person.city,'EmailAddress': self.person.emailAdress,'Username': self.person.username,'TelephoneNumber': self.person.telephoneNumber,},'book': self.book.toDict()}

    def DisplayLoan(self):
        return(self.book.displayBook()+"\n" + self.person.display() + "-----------------------------------------------\n")

class LoanAdministration:
    
    def __init__(self):
        self.ListofLoans = []
        with open(JSON_PATH,'r') as f:
            allLoans = json.load(f)
            if allLoans != None:
#                looping through all the loans
                for loanDict in allLoans:
                    Book1 = loanDict['book']
                    book1 = books.Book(Book1['ISBN'], Book1['author'], Book1['country'], Book1['language'], Book1['imagelink'], Book1['link'], Book1['pages'], Book1['title'], Book1['year'])
                    
                    subscriber = loanDict['person']
                    person1 = person.Person(subscriber['Number'], subscriber['Gender'], subscriber['NameSet'], subscriber['GivenName'], subscriber['Surname'], subscriber['StreetAddress'], subscriber['ZipCode'], subscriber['City'], subscriber['EmailAddress'], subscriber['Username'], subscriber['TelephoneNumber'])
                    
                    self.ListofLoans.append(Loan(book1,person1))


    def AddLoan(self, book, person):
        loan = Loan(book,person)
        self.ListofLoans.append(loan)
        self._saveLoans()

    def RemoveLoan(self,title,username):
        for loan in self.ListofLoans:
            if loan.person.username == username and loan.book.title == title:
                self.ListofLoans.remove(loan)
        self._saveLoans()

    def _saveLoans(self):
        #save the book list to json
        Loan_dict_list = [b.toDict() for b in self.ListofLoans]
        os.unlink(JSON_PATH) 
        with open(JSON_PATH, 'w+') as f:
            json.dump(Loan_dict_list, f)