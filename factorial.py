"""
 Write a Python program using a recursive function to calculate the factorial of a number. 
 A recursive function is a function that calls itself to solve a problem.
"""
# Recursive function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ask user for input
user_input = float(input("Enter a number to calculate its factorial: "))

# Call the function and print the result
print(f"The factorial of {user_input} is {factorial(int(user_input))}.")
