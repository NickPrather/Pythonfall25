"""

Create a program named personal_diary.py.
Ask the user for date, time, and a diary entry.
Append the entry to diary.txt (do not overwrite).
Separate each entry with a blank line for readability.
Run your program at least three times to confirm new entries are saved properly


"""




# pulls info from datetime module from pythons library
from datetime import date, time


def save_entry(date, time, entry):
    try: # try block to attempt to open the file and write it
        with open("journal.txt","a") as file:
            file.write(f"date: {date}\ntime: {time}\nentry: {entry}")
            file.write("\n")  # spacer line for clarity
    except: # exception line in case there is a problem with the file
        print("error with the diary")
def main(): # main function that gets user data and saves it
    date = input("enter the date of entry ex: mm/dd/yyyy: ")
    time = input("enter the time of entry ex: hh:mm am/pm: ")
    entry = input("write your diary entry here: ")
    lines = [] # list to hold the lines of entry
    while True: # loop that allows the user to give multiple lined in their entry
        line = input()
        if line == "":
            break
        lines.append(line) # adds each line to the list
        entry = "\n".join(lines) # joins lines together but puts a new line in between
    if entry.strip() == "": # if statement to see if the user entered anything
        print("No diary entry entered. Nothing was saved") # checks to see if the user entered anything
    else: # else statement to confirm the saved entry
        save_entry(date, time, entry)
        print("diary entry saved") # tells the user their entry is saves


        
    


main()
