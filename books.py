import json
import os
from pathlib import Path

#json path
JSON_PATH = str(Path(__file__).parent / 'booksset1.json')

class Book:
    

    
    def __init__(self, ISBN, author, country, language, imageLink, link, pages, title, year):
        self.ISBN = ISBN
        self.author = author
        self.country = country
        self.language = language
        self.imageLink = imageLink
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year
        
    def toDict(self):
        return {
            'ISBN': self.ISBN, 'author': self.author, 'country': self.country, 'language': self.language, 
            'imagelink': self.imageLink, 'link': self.link, 'pages': self.pages, 'title': self.title, 'year': self.year }

        
    
    def displayBook(self):
        return("Title: %s\nAuthor: %s\nYear: %i\nLanguage: %s\nCountry: %s\nPages: %i\n" % (self.title, self.author, self.year, self.language, self.country, self.pages))

    
    
class Books:
    
    def __init__(self):
        self.bookList = []
        with open(JSON_PATH,'r') as f:
            allBooks = json.load(f)
        #looping through all the books
        for bookDict in allBooks:
            self.bookList.append(Book(
                None, bookDict["author"], bookDict["country"], bookDict["language"], bookDict["imagelink"], 
                bookDict["link"], bookDict["pages"], bookDict["title"], bookDict["year"]))

   


    def addBook(self):
        print("Add a book")
        print("ISBN:")
        newISBN = int(input())
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

        #saving new book to the list
        self.bookList.append(Book(newISBN, newAuthor, newCountry, newLanguage, newimageLink, newLink, newPages, newTitle, newYear))
        self._saveBooks()
    
    def _saveBooks(self):
        #save the book list to json
        book_dict_list = [b.toDict() for b in self.bookList]
        os.unlink(JSON_PATH) 
        with open(JSON_PATH, 'w+') as f:
            json.dump(book_dict_list, f)


    def deleteBooks(self):
        print("Delete a book\nEnter the title: ")
        
        



