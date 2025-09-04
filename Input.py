"""
Create a Python application that allows users to input their total budget and 
the amount spent in various categories. The program will then calculate and display 
the percentage of the total budget each category represents.
"""
#Asks user for income
income = input("enter your monthly income: ")
income = int(income)

# asks user for housing costs
housing = input("enter your housing expenses: ")
housing = int(housing)

# asks user for grocery costs
groceries = input("enter your food expenses: ")
groceries = int(groceries)

# asks user for transportation costs
transportation = input("enter your transportation expenses: ")
transportation = int(transportation)
# asks user for health care costs
healthcare = input("enter your healthcare expenses: ")
healthcare = int(healthcare)

# asks user for personal care costs
personalcare = input("enter your personal care expenses: ")
personalcare = int(personalcare)

# asks user for clothing costs
clothing = input("enter your clothing expenses: ")
clothing = int(clothing)

# asks user for debt costs
debt = input("enter your debt expenses: ")
debt = int(debt)

#calculates expense percentages
housing_percentage = (housing / income) * 100
groceries_percentage = (groceries / income) * 100
transportation_percentage = (transportation / income) * 100
healthcare_percentage = (healthcare / income) * 100
personalcare_percentage = (personalcare / income) * 100
clothing_percentage = (clothing / income) * 100
debt_percentage = (debt / income) * 100

#printing expense percentages
print("Expense Percentages:")
print(f"Housing: {housing_percentage:.2f}%")
print(f"Groceries: {groceries_percentage:.2f}%")
print(f"Transportation: {transportation_percentage:.2f}%")
print(f"Healthcare: {healthcare_percentage:.2f}%")
print(f"Personal Care: {personalcare_percentage:.2f}%")
print(f"Clothing: {clothing_percentage:.2f}%")
print(f"Debt: {debt_percentage:.2f}%")
# found out .2f means 2 decimal places so i implemented them to improve my clarity


# total money left over
total_expenses = housing + groceries + transportation + healthcare + personalcare + clothing + debt
saving_money = income - total_expenses
print(f"Total money left over: ${saving_money}")
