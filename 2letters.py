"""

Define a generator function two_letter_combinations that takes a list of characters as an argument.
Use nested loops within the generator function to iterate over the list of characters. 
In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination.
In the main method, call the generator function with a list of characters and iterate over the 
generator to print each combination. Create an original  5-letter list.
Include comments in your code to explain the logic behind the generator function and the use of the yield statement.
 
"""


# function to generate two letter combinations #  I aided with chat gpt in order to find a way to assemble thhe two characters
def two_letter_combinations(characters):
       for first in characters:        # Loop through each character So it gets its first letter
        for second in characters:   # loop through Each character so it gets it's second letter
            yield first + second    # yield the combination instead of returning a full list

# main function that calls the generator function   
def main():
      characters = ['A','B','C','D',] # My four letter list
      for combination in two_letter_combinations(characters): # calls the generator function and goes through the result through the result
            print(combination) # print the two Letter combinations

main()
