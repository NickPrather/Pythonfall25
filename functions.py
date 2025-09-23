"""

Write a Python program that includes two functions -
 one to calculate the area of a square and another for the area of a circle.
"""
# function to caluculate the area of a square
def square(side):
    print("The area of the square is", side * side)
   
  # function to calculate the area of a circle

def circle(radius):
    print("the area of the circle is", 3.14 * radius * radius)

# taking inputs from the user
side = float(input("enter the length of the side of the square: "))

radius = float(input("enter the radius of the circle: "))
# calls the functions
square(side)
circle(radius)
