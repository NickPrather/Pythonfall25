"""

File 1: Write an Employee class with the following attributes:

Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:

Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class.

Assignment Part 2: Implementing and Testing
 

Part 2: Write a script to:

Create an instance of ProductionWorker.
Prompt the user for each attribute's data.
Store and then display the data using the object's method



"""

# creates employee class that holds the user information
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
# gets and sets name and number
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def __str__(self):
        return (f"Name: {self.__name} Employee Number: {self.__number}")
# creates class for production worker where information will inherited from worker  
class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate
#gets user shift number
    def get_shift_number(self):
        return self.__shift_number
#gets user pay rate
    def get_pay_rate(self):
        return self.__pay_rate
# sets user shift number
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
# sets user pay rate
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
# function that checks to see if user inputted a 1 or 2 for day or night shift
    def get_shift_name(self):
        if self.__shift_number == 1:
            return "Day"
        elif self.__shift_number == 2:
            return "Night"
        else:
            return "Invalid shift"
# function that takes the users info and turns it into a readable string
# used the /n to create new lines for added clarity
    def __str__(self):
        return (f"Name: {self.get_name()}\n"
            f"Employee Number: {self.get_number()}\n"
            f"Shift: {self.get_shift_name()}\n"
            f"Pay Rate: {self.__pay_rate}")
# main function that prompts user to enter information and then creates an object out of the information then prints all the details   
def main():
        print("Enter the following details of the Employee")
print("--------------------------------------------") # spacer line for clarity
# asks user for their input and worker information
name = input("Enter Employee Name: ")
number = input("Enter Employee Number: ")
pay_rate = float(input("Enter Pay Rate: "))
shift_number = int(input("Enter Shift Number (1 = Day, 2 = Night): "))

print("-------------------------------------------------------") # spacer line for clarity
worker = ProductionWorker(name, number, shift_number, pay_rate) # creates production worker out of the data we collected
# prints the information of the employee
print("Details of Employee:")
print(worker)
print("-------------------------------------------------------")

# calls main function to run the program
main()




