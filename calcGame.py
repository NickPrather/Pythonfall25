"""
Write a short interactive Python program of your choice that uses try and except to catch and respond to at least
 two specific exceptions. Your program should:

Include a main() function.
Use try and except to catch specific errors like ValueError or ZeroDivisionError.
Provide helpful messages when errors occur.
Do something meaningful or fun—be creative! You could build a number guessing game, 
a basic calculator, or even a simple quiz with input validation.

"""

def calculator_game():
    print("Calculator Game")
# try block that gets the users two numbers and if one or both arent numbers it creates a value error
    try:
        number1 = float(input("please enter a number: "))
        number2 = float(input("please enter a second number: "))
    except ValueError:
        print("That is not a number")
        return
    # had chat gpt help me figure out a system to select a way for the user to select a operation
    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
# gives the user a choice on what number to  select that is linked to each operation
    choice = input("Enter 1, 2, 3, or 4: ")
    try:
        if choice == "1":
            result = number1 + number2
        elif choice == "2":
            result = number1 - number2
        elif choice == "3":
            result = number1 * number2
        elif choice == "4":
            result = number1 / number2
        else:
            print("Invalid operations please enter a number 1-4")
            return
    except ZeroDivisionError:
        print("you cannot divide by 0")
        return
    print(f"the result is{result}")
    # runs the main function of the program
calculator_game()

        




