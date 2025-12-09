"""
Restaurant Ordering Game
Nick Prather
Course: ADD 100
Section: 004
Date: 11/10/2025

Plan:
This is a restaurant ordering program that will display a menu with prices, 
allow user to order what items they would want, track the users order, and form a organized receipt 
that displays the final price of the order. and finally display a thank you message.
"""
from menu import Menu
from order import Order
from receipt import Receipt
def main():  # main function to run the game
     """
    main function that runs the restraunt ordering game
    first it loads the menu from the text file then it displays the menu to the user
    then it allows the user to order items until they type 'done'
    then it generates, saves, and displays the recipt to the user.
    """

    menu = Menu() 
    menu.load_menu("menu_items.txt")  # Fixed: removed incorrect directory prefix 
    order = Order() # creates an order object
    while True: # loops until the user is done ordering
        menu.display_menu(menu.get_items()) # outputs the menu to user
        choice = input("Enter item name to order (or 'done' to finish): ") # gets the user's choice
        if choice.lower() == 'done': 
            break
        quantity = int(input("Enter quantity: ")) 

        for category, name, price in menu.get_items():
            if name.lower() == choice.lower(): 
                order.add_item(name, price, quantity) 
                print(f"Added {quantity}  {name} to your order.\n") 
                break
        else: # if the item is not found on the menu
            print("Item not found. Please try again.\n")
    receipt = Receipt(order) # creates a receipt object
    print(receipt.generate_receipt()) 
    receipt.save_receipt("receipt.txt") 


main() # runs the main function

"""
how i found how to use a with open statement:
https://www.geeksforgeeks.org/python/how-to-open-a-file-using-the-with-statement/

how i found a add_item method:
https://www.geeksforgeeks.org/python/set-add-python/




"""
