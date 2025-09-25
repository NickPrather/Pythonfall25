"""

Develop a Python-based Madlib based on a song of your choice. 
The program should collect at least 8 different pieces of information from the user 
and incorporate them into the song using named 
arguments. The goal is to practice using functions, user input, and string manipulation in Python.
"""
def custom_song():
    # Run the input function
    get_input()

# function that gets the input from the user
def get_input():
    star = input("Enter a Object: ")   
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    adj1 = input("Enter an thing: ") 
    adj2 = input("Enter another verb: ")
    place = input("Enter a place: ")
# call the story function 
    story(star, verb1, verb2, noun1, noun2, adj1, adj2, place)

# function that puts the user input into the song
def story(star_in, verb1_in, verb2_in, noun1_in, noun2_in, adj1_in, adj2_in, place_in):
    print(f"\n🎵 Twinkle, twinkle, little {star_in}")
    print(f"How I {verb1_in} what you are")
    print(f"Up above the {noun1_in} so high")
    print(f"Like a {adj1_in} {noun2_in} in the sky")
    print(f"Twinkle, twinkle, little {star_in}")
    print(f"How I {verb2_in} what you are")
    print(f"When the {adj2_in} sun is gone over {place_in} 🎵")

# main function that runs the program
def main():
    custom_song()

# run the main function
main()
