"""

In this exercise, you will practice using logical operators (and, or, not) in Python. 
Your task is to create a program that prompts 
the user for two integer inputs and then demonstrate the use of these operators.
"""

number = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))

if number > 3 and number2 > 3:
    print("Both numbers are greater than 3. True")
else:
    print("Both numbers are not greater than 3. False")
if number == 16 and number2 == 16:
    print("both numbers are equal to 16. True")
else:
    print("both numbers are not equal to 16. False")
if number <= 10 or number2 <= 10:
    print("At least one number is less than or equal to 10. True")
else:
    print("Both numbers are greater than 10. False")
if number > number2 or number2 > number:
    print("One number is greater than the other. True")
else:
    print("Both numbers are equal. False")
if number >= 100 and not number2 >= 100:
    print("One number is greater than 100. True")
else:
    print("Both numbers are less than 100. False")
if not number == number2:
    print("The numbers are not equal. True")
else:
    print("The numbers are equal. False")
