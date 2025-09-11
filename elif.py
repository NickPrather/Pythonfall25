"""

Accept a numeric grade from the user and display a 
letter grade. The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F
"""
# accepts the users grade and turns it into a variable
grade = int(input("Enter your grade: "))
# if and elif statements to see what letter grade the user gets
if grade >= 90 and grade <= 100:
    print("your grade is an A")
elif grade >= 80 and grade < 90:
    print("your grade is a B")
elif grade >= 70 and grade < 80:
    print("your grade is a C")
elif grade >= 60 and grade < 70:
    print("your grade is a D")
elif grade < 60:
    print("your grade is an F")
