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
import os 
file_path = "Final_project.py/menu_items.txt"
class Menu:
# initializes the menu with an empty list of items
    def __init__(self):
        self.items = []
# gets items from menu
    def get_items(self):
        return self.items
# sets items for menu
    def set_items(self, new_items):

        self.items = new_items # loads menu from file

    def load_menu(self, file_name):
        with open(file_name, "r") as file:
            next(file)  # skip header

            for line in file:
                data = line.strip().split(",") # splits data with a comma
                category = data[0] 
                name = data[1] 
                price = float(data[2]) # gets price from data
                self.items.append((category, name, price)) # appends the data to the list of items
# displays the menu to the user
    def display_menu(self, new_items):
        self.items = new_items
        print("\nMENU") # prints the menu header fro clarity

        categories = set([item[0] for item in self.items]) 
# displays items by catagory
        for cat in categories:
            print(f"\n{cat.upper()}:") # prints catgory header in uppercase
            for c, name, price in self.items: # loops through items

                if c == cat: # check if item catagory matches current catagory
                    print(f" - {name}: ${price:.2f}") 
        print()
# order class to track what the user orders
class Order:
# tracks the users order
    def __init__(self):

        self.order_items = [] # empty list to hold the order items
# gets the order items
    def get_order_items(self):
        return self.order_items # returns item
    def set_order_items(self, new_items): 
        self.order_items = new_items  
    def add_item(self, item_name, price, quantity): # adds an item 

        self.order_items.append((item_name, price, quantity)) 
    def remove_item(self, item_name):

        self.order_items = [item for item in self.order_items if item[0] != item_name] # removes an item from the order
    def calculate_total(self): 
        total = 0
        for name, price, qty in self.order_items: # loops through the order items
            total += price * qty

        return total 
# receipt class to generate and save the receipt
class Receipt:

    def __init__(self, order):


        self.order = order 
    def generate_receipt(self): 
        receipt = "\n------RECEIPT-------\n" # receipt header and = signs for clarity
        for name, price, quantity in self.order.get_order_items(): # loops through the order items
            line_total = price * quantity
            receipt += f"{name} x{quantity} - ${line_total:.2f}\n" # adds the item to the receipt

        total = self.order.calculate_total() # calculates the total price of the order
        receipt += f"\nTOTAL: ${total:.2f}\n" # adds the total to the receipt
        receipt += "Thank you for your order!\n" 
        return receipt # returns the receipt
    def save_receipt(self, file_name): 
        with open(file_name, "w") as file: # opens the file in write mode

            file.write(self.generate_receipt()) # writes the receipt to the file
def main(): # main function to run the game+fe21s``
    menu = Menu() 
    menu.load_menu("menu_items.txt") 
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