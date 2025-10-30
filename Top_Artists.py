"""
Write a Python program that handles exceptions related to list operations. 
Your program will start with a predefined list of the top ten performing artists of all 
time and will include functionality to modify this list based on user input.
"""
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley",
                   "Mariah Carey", "Stevie Wonder", "Janet Jackson",
                   "Michael Jackson", "Whitney Houston", "Rihanna"]
    # Your code goes here
    print("List of top artists:")
    # prints the list of top artists
    print(top_artists)
    # calls the modify artist function
    modify_artist(top_artists)
    # uses /n for a line spacer and tells user the list is coming
    print("\nUpdated list:")
    # displays users new updates list
    print(top_artists)

# modify artists list function that allows the user to input their new top artist
def modify_artist(artist_list):
    # try block that lets the user input the index number and the name of the new artists 
    try:
        index = int(input("Enter the index number of the artist to replace (0-30): "))
        new_artist = input("Enter the new artist name: ")
        # replaces the old artists name with the new one and updates the list
        artist_list[index] = new_artist
        # except block that works when you enter a invalid index for a non-artist name
    except (ValueError, IndexError):
        print("Please enter a valid index value.")
        # main function that contains the original list
main()
