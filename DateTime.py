"""

Ask the user to input their birthday.
Calculate the user's age in years, months, days, hours, and minutes.
Provide detailed comments to all of the code, explaining what each line that has to do with time calculation does.
Display the results in a user-friendly format.
Implement the solution inside a main() function.


"""
from datetime import datetime
# main function that runs the program
def main():
   
    print("\n\n")
    try:
        today = datetime.today() # gets the current date and time

        # input from user
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))

        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        delta = today - birthday # claculates the difference between today and the users birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425
       
        print(f'You are {delta_years} years old')
       
        delta_months = (delta.days / 365.2425) * 12 # claculates the users age in months
        print(f'You are about {int(delta_months)} months old')

        delta_weeks = delta.days / 7 # claculates the users age in weeks
        print(f'you are {int(delta_weeks)} weeks old')

      
    except Exception as e: # exception handling for any errors 
        print(f"ooooops!!!:  {e}") 
        main()
main()
