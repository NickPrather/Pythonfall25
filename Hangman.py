"""
Hangman Start - Week 10 Strings Demo

This program begins a simple version of Hangman. You will finish it by:
- Adding a list to keep track of guessed letters
- Checking if the letter was already guessed BEFORE checking if it is in the word ( give them feedback)
- Changing the word list to 15 words on a subject of your choice
- Display how many incorrect guesses they have left 
- validate data entry (actual letter? only 1 letter?)
- use a try and except statement around data entry
"""

import random
# My word list of 15 Hockey teams
WORD_LIST = ("BlackHawks","RedWings", "Wild","GoldenKnights","Predators","Panthers","Rangers","Kraken","BlueJackets","MapleLeafs","Jets","Oilers","Devils","Hurricanes","Flames")
# Game function that holds all the code to make the game work
def game(answer, display):
    wrong = 0
    right = 0
    guessed_letters = []
    max_wrong = 5

    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")
# keeps game running till you win or lose
    while True:
        for item in display:
            print(item, end=" ")
        print("\n\n")

        guess = input("Please enter a letter: ").upper()
# checks to see if a non letter or multiple letters were entered
        if not guess.isalpha():
            print("Please enter a letter")
            continue
        if len(guess) != 1:
            print("Please enter 1 letter")
            continue
# checks to see if you have already guessed this letter and if you havent it adds it to the guessed letters list
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        else:
            guessed_letters.append(guess)
# checks to see if the guessed letter is in the word
        bad_guess = True
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess
                bad_guess = False
# if guessed letter is wrong this takes away a guess and prints wrong 
        if bad_guess:
            print("Wrong!")
            wrong += 1
        else:
            # if letter is correct it prints correct
            print("Correct!")

        print(f"You have {max_wrong - wrong} guesses left")
# displays to show you won the game
        if "_" not in display:
            print("You Win!")
            print("The word was:", answer)
            break
# tells you that you lost and gives you the word
        if wrong >= max_wrong:
            print("You Lose!")
            print("The correct word was:", answer)
            break
# main function that run the above program
def main():
    answer = random.choice(WORD_LIST).upper()
    display = ["_"] * len(answer)
    game(answer, display)

main()
