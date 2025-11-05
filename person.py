"""

Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods 
allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. 
Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance.
 Ensure the output is formatted and easy to read. You need to print out all the data for each. 
 You can create a method that prints everything or call each get function one at a time.

"""
# Class definition for person
class Person:
    def __init__(self, name, address, age, phone_number):
        self.name = name # private variable for name
        self.address = address # private variable for address
        self.age = age # private variable for age
        self.phone_number = phone_number # private variable for phone number

    def get_name(self):
        return self.name # prints persons name

    def get_address(self):
        return self.address # prints persons address 

    def get_age(self):
        return self.age # prints persons age

    def get_phone_number(self):
        return self.phone_number # prints persons phone number
    
    def set_name(self, name):
        self.name = name  # updates the name

    def set_address(self, address):
        self.address = address # updates the address

    def set_age(self, age):
        self.age = age # updates the age

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number # updates the phone number
# prints all the peoples data in a clear manor
    def get_info(self):
            return f"Name: {self.name}, Address: {self.address}, Age: {self.age}, Phone: {self.phone_number}"

# creates all three people and their information
person1 = Person("John Smith", "486 Maple Dr", 61, "847-367-1234")
person2 = Person("Tyler Locket", "147 Oakland Ave", 33, "815-673-5678")
person3 = Person("Kevin Parker", "193 Pine ridge Dr", 39, "224-967-9012")
# calls the functions
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
