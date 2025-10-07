"""

Write a Python program that simulates a Magic 8-Ball. The program should:

Store at least 20 possible answers in a list.
Prompt the user to ask a yes-or-no question.
Select and display a random answer from the list.
Continue asking questions in a loop until the user chooses to stop.
"""
# importing random module to select a random response from the list
import random
# function to return a list of responses
def magic8_ball():
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes.",
        "No.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My response is no.",
        "My sources say no.",
        "Doesn't look good.",
        "Outlook not so good.",
        "Very unlikely.",
        "Absolutely.",
        "Of course yes.",
        "Yes definitely.",
        "You can count on it.",
        "Most definitely.",
        "From what I know, yes."
    ]
    # returns responses list so i can use it in the main function
    return responses  
# main function to run the program
def main():
    responses = magic8_ball()
    # loop to keep asking question until the user is done
    while True:
        question = input("Ask the Magic 8 Ball a question: ")
        answer = random.choice(responses)
        print("Magic 8 Ball says: " + answer)
        # asks user if they want to ask more questions
        again = input("Do you want to ask another question? (yes/no): ")
        # breaks the loop if user says no
        # also handles case sensitivity
        if again.lower() == 'no':
            print("Goodbye.")
            # breaks the loop
            break
# calls the main function to run the program
main()
