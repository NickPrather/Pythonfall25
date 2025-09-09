"""
Write a Python program that uses if-else statements and:

Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.
"""
# asking for user age
age = int(input("How old are you?"))
# if/else statements to see what user is eligible for
if age >= 16:
    print("you are old enough to drive.")
else:
    print("you are not old enough to drive.")
if age >= 18:
    print("you are old enough to vote.")
else:
    print("you are not old enough to vote.")
if age >= 21:
    print("you are old enough to buy alcohol.")
else:
    print("you are not old enough to buy alcohol.")
if age >= 65:
    print("you are eligible for a senior discount.")
else:
    print("you are not eligible for a senior discount.")

