import Companies

class Subscriber(Companies.PublishingCompany):
    @staticmethod
    def Smenu(username):
        while True:
            print("\nPlease enter a number that stand before the action you want to do")
            print("[1] See all available books\n[2] Search for a book\n[3] Loan a book\n[4] Exit")
            userInput = input()
            if userInput == "1":
                Subscriber.SeeBooks()
            elif userInput == "2":
                Subscriber.SearchBook()
            elif userInput == "3":
                Subscriber.LoanBook()
            elif userInput == "4":
                break
    
    @staticmethod
    def LoanBook():
        print("loan a book")