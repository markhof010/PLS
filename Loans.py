import books
import person

class Loan:
    
    def __init__(self, book, person):
        self.person = person
        self.book = book

    def DisplayLoan(self):
        print(self.book.displayBook()+"\n"+ self.person.display())

class LoanAdministration:
    
    def __init__(self):
        self.ListofLoans = []

    def AddLoan(self, book, person):
        loan = Loan(book,person)
        self.ListofLoans.append(loan)

    def RemoveLoan(self,title,username):
        for loan in self.ListofLoans:
            if loan.person.username == username and loan.book.title == title:
                self.ListofLoans.remove(loan)