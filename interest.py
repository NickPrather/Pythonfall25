"""

Write a Python function named calculate_interest that computes and returns simple interest based on given parameters. 
(Note - you will call the function from the main() function, main is required!
"""
# function that calculates simple interest
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    # return the interest
    return interest
# main function that runs the program
def main():
    principal = float(input("enter the principal amount: "))
    rate = float(input("enter the rate of interest: "))
    time = float(input("enter the time in years: "))
    interest = calculate_interest(principal, rate, time)
    # prints the interest rate and all the calculated values
    print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
    return interest
# calls the main function
main()
