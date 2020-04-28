import os
import platform
import customer
import Companies
import librarian

def ClearFun():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

while True:
    print("[1] Subscriber\n[2] Publishing company\n[3] Librarian")
    personLogin = input("Please enter a number that stand before the choices: ")

    if personLogin == "1":
        username = input("Please enter your username: ")
        ClearFun()
        customer.Subscriber.Smenu(username)

    elif personLogin == "2":
        print("PublishingCompany")
        #call class PublishingCompany
        Companies.PublishingCompany.PCmenu()

    elif personLogin == "3":
        while True:
            loginName = input("Please enter your username:\n")
            password = input("Please enter the password:\n")
            if loginName == "librarian" and password == "librarian":
                ClearFun()
                librarian.Librarian.Lmenu()
                break
                #call class Librarian
            elif loginName != "librarian":
                print("Wrong username!")
            elif password != "librarian":
                print("Wrong password!")
