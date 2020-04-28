class PublishingCompany:
    @staticmethod
    def PCmenu():
        while True:
            print("\nPlease enter a number that stand before the action you want to do")
            print("[1] See all available books\n[2] Search for a book\n[3] Exit")
            userInput = input()
            if userInput == "1":
                PublishingCompany.SeeBooks()
            elif userInput == "2":
                PublishingCompany.SearchBook()
            elif userInput == "4":
                break

    @staticmethod
    def SeeBooks():
        print("see all books")

    @staticmethod
    def SearchBook():
        print("search a book")