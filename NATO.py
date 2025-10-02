"""
Your mission is to create a Python program that uses a dictionary to translate letters 
into the NATO Phonetic Alphabet. This program will ask users for a word
 and then spell it out using the NATO codes.
"""

# create a dictionary that maps letters to their NATO equivalents

nato_alphabet = {
    "A": "alpha",
    "B": "bravo",
    "C": "charlie",
    "D": "delta",
    "E": "echo",
    "F": "foxtrot",
    "G": "golf",
    "H": "hotel",
    "I": "india",
    "J": "juliett",
    "K": "kilo",
    "L": "lima",
    "M": "mike",
    "N": "november",
    "O": "oscar",
    "P": "papa",
    "Q": "quebec",
    "R": "romeo",
    "S": "sierra",
    "T": "tango",
    "U": "uniform",
    "V": "victor",
    "W": "whiskey",
    "X": "x-ray",
    "Y": "yankee",
    "Z": "zulu"
    }


# define the main function
def main():
    word = input("Enter a word: ").upper()
    # separate function to get the nato translation
    def get_nato_translation():
        for letter in word:
            # check to ensure the letter is in the dictionary
            nato_translation = nato_alphabet.get(letter, letter) #uses 2 arguments first argument checks to see if the letter is in the dictionary if not the second argument just returns the letter.
            # print the nato equivalent
            print(nato_translation)
    get_nato_translation()
# separate function that calls main and runs the program
def run_program():
    main()
# calls the function to run the program
run_program()
