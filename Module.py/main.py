from math_operations import Calculator, geometry


result = Calculator.add(5, 3)
print("Addition result:", result)

result = Calculator.subtract(10, 4)
print("Subtraction result:", result)


result = geometry.area_square(5)
print("Area of a square: ", result)

result  = geometry.area_circle(2)
print("Area of a circle: ", result)

result = geometry.area_triangle(6, 7)
print("Area of a triangle: ", result)
