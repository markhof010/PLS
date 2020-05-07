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
        
# Create 3 users
person1 = Person(1, "Male", "FB", "Ferdi", "Bilgic", "Van Ravesteyn Erf, 430", "3315 DT", "Dordrecht", "0984562@hr.nl", "FBHR", "06123456789")
person2 = Person(2, "Female", "DC", "Jane", "Doe", "Van Dirk Erf, 220", "5524 TD", "Utrecht", "213456@hr.nl", "JaneDoe", "06987654321")
person3 = Person(3, "Male", "WO", "John", "Doe", "Van Jan Erf, 124", "3452 PR", "Amsterdam", "84657@hr.nl", "JohnDoeeee", "067382374")
#person4 = Person.from_input()

# Display the users
person1.display()
person2.display()
person3.display()

# Create a list object and save the users in there
mypersons = personList()
mypersons.add(person1)
mypersons.add(person2)
mypersons.add(Person.from_input())
mypersons.remove(person2)


# Display all the users
mypersons.show()
