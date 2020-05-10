import os
import platform
import customer
import Companies
import librarian
import books
import Loans
import person

def ClearFun():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

BookList = books.Books()
LoanList = Loans.LoanAdministration()
PersonList = person.PersonList()

while True:
    print("[1] Subscriber\n[2] Publishing company\n[3] Librarian")
    personLogin = input("Please enter a number that stand before the choices: ")

    if personLogin == "1":
        username = input("Please enter your username: ")
        ClearFun()
        customer.Subscriber.Smenu(username,BookList, LoanList, PersonList)

    elif personLogin == "2":
        print("PublishingCompany")
        #call class PublishingCompany
        Companies.PublishingCompany.PCmenu(BookList)

    elif personLogin == "3":
        while True:
             loginName = input("Please enter your username:\n")
             password = input("Please enter the password:\n")
             if loginName == "librarian" and password == "librarian":
                 ClearFun()
                 librarian.Librarian.Lmenu(BookList, LoanList, PersonList)
                 break
             elif loginName != "librarian":
                 print("Wrong username!")
             elif password != "librarian":
                 print("Wrong password!")
            #librarian.Librarian.Lmenu(BookList, LoanList, PersonList)
