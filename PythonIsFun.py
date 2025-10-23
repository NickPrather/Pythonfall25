"""
There is a Python file string_methods2.py Download string_methods2.
pythat you need to download. This file contains several TODO comments,
 each indicating a small task for you to complete.
"""
# Python String Methods Practice
# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
# Your code here
print(string1.capitalize())
# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> " python "
string2 = "python"
# Your code here
print(string2.center(10))
# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
# Your code here
print(string3.endswith("on"))
# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
# Your code here
print(string4.find("th"))
# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
# Your code here
print(string5.isalnum())
# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
# Your code here
print(string6.isalpha())
# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
# Your code here
print(string7.islower())
# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if " " is all whitespace
string8 = " "
# Your code here
print(string8.isspace())
# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
# Your code here
print(string9.isupper())
# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
print(separator.join(iterable1))
