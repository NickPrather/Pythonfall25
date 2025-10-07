"""

 Enhance a basic Python program by implementing 
 try and except statements to handle errors in user input, focusing on data type errors.
"""

# Simple Python program to calculate the square of a number

def square_number():
    # gets user input and squares the number
    # try and except to handle the error if input is not a number
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
# calls the function to run the program
square_number()
