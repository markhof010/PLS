import csv
import librarian
import customer

while True:
    print("Log in:\nPlease enter your username and password as librarian (username password)\nPlease enter your username as customer")
    login = input()
    try:
        Login = login.split()
        name = Login[0]
        password = Login[1]

        if name == "mark" and password == "1998":
            librarian.menu()

    except IndexError:
        f = open(r'C:\\Users\\mark\Documents\\HogeSchool\\analyse\Assignments\\PLS\\FakeNameSet20.csv')
        Reader = csv.reader(f)

        for row in Reader:
            if login == row[9]:
                customer.menu(login)
                    
        f.close()

