# A simple class to make the subscriber
class Person:
    def __init__(self, number, gender, nameSet, givenName, surname, streetAdress, zipCode, city, emailAdress, username, telephoneNumber):
        self.number = number
        self.gender = gender
        self.nameSet = nameSet
        self.givenName = givenName
        self.surname = surname
        self.streetAdress = streetAdress
        self.zipCode = zipCode
        self.city = city
        self.emailAdress = emailAdress
        self.username = username
        self.telephoneNumber = telephoneNumber

    @classmethod
    def from_input(cls):
        return cls(
            int(input('PERSON ID: ')),
            input('GENDER: '), 
            input('NAMESET: '),
            input('GIVENNAME: '), 
            input('SURNAME: '),
            input('STREET: '), 
            input('ZIPCODE: '),
            input('CITY: '), 
            input('EMAIL: '),
            input('USERNAME: '), 
            input('TELEPHONE: ')
        )    
        
    def display(self):
        print("PERSON ID: %d, GENDER: %s, NAMESET: %s, GIVENNAME: %s, SURNAME: %s, STREET: %s, ZIPCODE: %s, CITY: %s, EMAIL: %s, USERNAME: %s, TELEPHONE: %s \n" % (self.number, self.gender, self.nameSet, self.givenName, self.surname, self.streetAdress, self.zipCode, self.city, self.emailAdress, self.username, self.telephoneNumber))

# A list to save the people in
class personList:
    def __init__(self):
        self.persons = []
        
    def add(self, person):
        self.persons.append(person)

    def remove(self, person):
        self.persons.remove(person)
        
    def show(self):
        print("This person list contains:")
        for b in self.persons:
            b.display()
