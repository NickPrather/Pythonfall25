"""
Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.
"""
# creates a list of seats numbered 1 to 20
seats = list(range(1, 21))
# loop to allow multiple seat selections until the user is done selecting
while True:
    print("available seats:", seats)
    picked = int(input("pick a seat enter 0 when you are done: "))
    if picked == 0:
        break
    if picked in seats:
        seats.remove(picked)
        print("seat number",picked,"has been sold to you")
    else:
        print("invalid seat please try again")
        
