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
        y = True
        while y:
            username = input("Please enter your username: ")
            for person in PersonList.nameList:
                if username == person.username:
                    ClearFun()
                    customer.Subscriber.Smenu(username,BookList, LoanList, PersonList)
                    y = False
                    break
            if y:
                print("Please enter a username that exists")

    elif personLogin == "2":
        print("PublishingCompany")
        #call class PublishingCompany
        Companies.PublishingCompany.PCmenu(BookList)

    elif personLogin == "3":
        while True:
            loginName = input("Please enter your username:\n")
            if loginName == "librarian":
                password = input("Please enter the password:\n")
                if password == "librarian":
                    ClearFun()
                    librarian.Librarian.Lmenu(BookList, LoanList, PersonList)
                    break
                else:
                    print("Wrong password!")
            else:
                print("Wrong username!")
            #librarian.Librarian.Lmenu(BookList, LoanList, PersonList)

    elif personLogin == "4":
        print(PersonList.nameList)
