import json
import csv

def showAllBook():
    with open(r'C:\\Users\\mark\Documents\\HogeSchool\\analyse\Assignments\\PLS\\booksset1.json') as f:
        data = json.load(f)
        
        for book in data:
            print(book["title"] + "     by " + book["author"])
    f.close()

def search():
     while True:
        print("Please give the search option\n[1] Search on title\n[2] Search on author\n[3] Exit search")
        searchOption = input()
        with open(r'/booksset1.json') as f:
            data = json.load(f)
            
            if searchOption == "1":
                print("Please enter the title")
                title = input()
                
                for book in data:
                    if title == book["title"]:
                        print("\nTitle: " + book["title"] + "\nAuthor: " + book["author"] + "\nLanguage: " + book["language"])
                f.close()

            elif searchOption == "2":
                print("Please enter the title")
                name = input()

                for book in data:
                    if name == book["author"]:
                        print("\nTitle: " + book["title"] + "\nAuthor: " + book["author"] + "\nLanguage: " + book["language"])

                f.close()
           
            elif searchOption == "3":
                f.close()
                break
   
def Loan(username):
    frBook = open(r'./booksset1.json')
    books = json.load(frBook)

    exist = False
    title = ""

    while True:
        if exist:
            break
        
        print("Please enter the title or type 'exit' to exit")
        title = input()

        if title == "exit":
            break
        else:
            

            for book in books:
                if book['title'] == title:
                    exist = True
                    break
            if not(exist):
                print("The titel is either spelled wrong or we don't have the book")
    
    frBook.close()
    
    if exist:
        frCust = open(r'./FakeNameSet20.csv')
        customers = csv.reader(frCust)
        FirstName = ""
        LastName = ""
        EmailAdress = ""
        TelefoonNumber = ""

        for customer in customers:
            if username == customer[9]:
                FirstName = customer[3]
                LastName = customer[4]
                EmailAdress = customer[8]
                TelefoonNumber = customer[10]

        frCust.close()
        
        newLoan =   {
                        "userName" : username,
                        "firstName" : FirstName,
                        "lastName" : LastName,
                        "emailAdress" : EmailAdress,
                        "telefoonNumber" : TelefoonNumber,
                        "title" : title
                    }

        


def addLoan(data):
    frLoan = open(r'C:\\Users\\mark\\Documents\\HogeSchool\\analyse\Assignments\\PLS\\Loans.json')
    loans = json.load(frLoan)
        
    loans.append(data)
        
    frLoan.close()

    fw = open(r'C:\\Users\\mark\\Documents\\HogeSchool\\analyse\Assignments\\PLS\\Loans.json','w')

    json.dump(loans,fw)

        fw.close()

def menu(username):
    while True:
        print("\nPlease enter a number that stand before the action you want to do")
        print("[1] See all available books\n[2] Search for a book\n[3] Loan a book\n[4] Exit")
        userInput = input()
        if userInput == "1":
            showAllBook()
        elif userInput == "2":
            search()
        elif userInput == "3":
            Loan(username)
        elif userInput == "4":
            break