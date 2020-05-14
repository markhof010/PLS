import json
import os
from pathlib import Path
import random

#json path
JSON_PATH = str(Path(__file__).parent / 'booksset1.json')

class Book:
    
    def __init__(self, ISBN, author, country, language, imageLink, link, pages, title, year, amount = None, loaned = None):
        self.ISBN = ISBN
        self.author = author
        self.country = country
        self.language = language
        self.imageLink = imageLink
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year
        if amount == None and loaned == None:
            self.amount = random.randint(1,3)
            self.loaned = 0
        else:
            self.amount = amount
            self.loaned = loaned
        
        
    def toDict(self):
        return {
            'ISBN': self.ISBN, 'author': self.author, 'country': self.country, 'language': self.language, 
            'imagelink': self.imageLink, 'link': self.link, 'pages': self.pages, 'title': self.title, 'year': self.year,'amount': self.amount,'loaned': self.loaned }

        
    
    def displayBook(self):
        Left = self.amount - self.loaned
        return("Title: %s\nAuthor: %s\nYear: %i\nLanguage: %s\nCountry: %s\nPages: %i\nBooks left: %i/%i\n" % (self.title, self.author, self.year, self.language, self.country, self.pages, Left,self.amount))

    
    
class Books:
    
    def __init__(self):
        self.bookList = []
        with open(JSON_PATH,'r') as f:
            allBooks = json.load(f)
        #looping through all the books
        for bookDict in allBooks:
            try:
                self.bookList.append(Book(self.ISBNMaker(bookDict["title"],bookDict["author"],bookDict["country"],bookDict["language"]), bookDict["author"], bookDict["country"], bookDict["language"], bookDict["imagelink"], 
                    bookDict["link"], bookDict["pages"], bookDict["title"], bookDict["year"],bookDict["amount"],bookDict["loaned"]))
            except:
                self.bookList.append(Book(self.ISBNMaker(bookDict["title"],bookDict["author"],bookDict["country"],bookDict["language"]), bookDict["author"], bookDict["country"], bookDict["language"], bookDict["imagelink"], 
                    bookDict["link"], bookDict["pages"], bookDict["title"], bookDict["year"]))
        self._saveBooks()

   
    def ISBNMaker(self,title,author,country,language):
        LetterDict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
        
        nameISBN = ""
        nameISBN = nameISBN + LetterDict[title[0].lower()]
        nameISBN = nameISBN + LetterDict[author[0].lower()]
        nameISBN = nameISBN + LetterDict[country[0].lower()]
        nameISBN = nameISBN + LetterDict[country[1].lower()]
        nameISBN = nameISBN + LetterDict[language[0].lower()]
        nameISBN = nameISBN + LetterDict[language[1].lower()]
        
        return int(nameISBN)


    def addBook(self):
        print("Add a book")
        print("Author:")
        newAuthor = input()
        print("Country:")
        newCountry = input()
        print("Language:")
        newLanguage = input()
        print("Image link: ")
        newimageLink = input()
        print("Link:")
        newLink = input()
        print("Pages:")
        newPages = int(input())
        print("Title:")
        newTitle = input()
        print("Year:")
        newYear = int(input())
        newISBN = self.ISBNMaker(newTitle,newAuthor,newCountry,newLanguage)
        print("Amount:")
        newAmount = int(input())
        newLoaned = 0
        #saving new book to the list
        self.bookList.append(Book(newISBN, newAuthor, newCountry, newLanguage, newimageLink, newLink, newPages, newTitle, newYear,newAmount,newLoaned))
        self._saveBooks()
    
    def _saveBooks(self):
        #save the book list to json
        book_dict_list = [b.toDict() for b in self.bookList]
        os.unlink(JSON_PATH) 
        with open(JSON_PATH, 'w+') as f:
            json.dump(book_dict_list, f)
