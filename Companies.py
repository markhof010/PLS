import books

class PublishingCompany:
    @staticmethod
    def PCmenu(BookList):
        while True:
            print("\nPlease enter a number that stand before the action you want to do")
            print("[1] See all available books\n[2] Search for a book\n[3] Exit")
            userInput = input()
            if userInput == "1":
                PublishingCompany.SeeBooks(BookList)
            elif userInput == "2":
                PublishingCompany.SearchBook(BookList)
            elif userInput == "3":
                break

    @staticmethod
    def SeeBooks(BookList):
        for book in BookList.bookList:
            print(book.displayBook())

    @staticmethod
    def SearchBook(BookList):
        print("\nPlease enter a number that stand before the action you want to do")
        print("[1] Search on title\n[2] Search on Author\n[3] Search on laguage\n[4] Search on country")
        choice = input()
        
        title = ""
        author = ""
        language = ""
        country = ""

        if choice == "1":
            title = input("Title:\n")
        elif choice == "2":
            author = input("Author:\n")
        elif choice == "3":
            language = input("Language:\n")
        elif choice == "4":
            country = input("Country:\n")
            
        for book in BookList.bookList:
            if title == book.title:
                print(book.displayBook())
            elif author == book.author:
                print(book.displayBook())
            elif language == book.language:
                print(book.displayBook())
            elif country == book.country:
                print(book.displayBook())
