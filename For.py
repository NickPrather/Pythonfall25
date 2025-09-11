"""
Write a Python program to find and print all numbers divisible 
by 7 between 1 and 300. Use a for loop and the modulus operator (%).
"""
# defines 7 as the starting point
x = 7
# for loop to get all numbers divisible by 7 and under 300
for x in range(7, 300):
    # if statement using the modulus operator to check if number is divisible by 7
    if x % 7 == 0:
        # prints the number if divisible by 7
        print(x)
