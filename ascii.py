"""
At the end of this lesson, students will be able to:

Convert a character to its ASCII value using Python.
Convert an ASCII value back to a character.
Implement input validation using loops and error handling.
"""
# main function that gets user input for ascii value
def main():
    user_input = input("enter a single character ")
    if len(user_input) != 1:
        print("error please enter one character")
        return
    # ord to function to get ascii value
    ascii_value = ord(user_input)
    print(f"the ascii value of '{user_input}' is {ascii_value}")
    try:
        ascii_input = int(input("Enter an ASCII value (32–127): "))
        if 32 <= ascii_input <= 127:
            # chr function to get the character from the users ascii input
            character = chr(ascii_input)
            print(f"the character for ascii value '{ascii_input}' is {character}")
        else:
            print("invalid number be sure to input a number between 32 and 127")
    except ValueError:
        print("error please enter a valid number")

main()
