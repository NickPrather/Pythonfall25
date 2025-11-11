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
from Menu_items import Menu_items
class Menu:
    """ Represents the restaurant's menu.
     Attributes:
        items (list): A list of available menu items.
     Key Methods:
        load_menu(file_name): Load menu data from a file.
        display_menu(): Print formatted menu items to the screen."""
    def __init__(self):
        """Initialize empty menu"""
        self.items = []

    def load_menu(self, Menu_items):
        """Load menu items from a file.
        Parameters: file_name (str): The file containing menu data.
        Returns: None"""
        pass

    def display_menu(self):
        """Display the menu items to the user in a formatted list.
         Returns: None"""
        pass


class Order:
    """Represents a user's order.
    Attributes: order_items (list): Items the user has selected.
    Key Methods: add_item(item_name, quantity): Add a menu item to the order.
        remove_item(item_name): Remove an item from the order.
        calculate_total(): Compute total cost of the order."""
    def __init__(self):
        """Initialize an empty order list."""
        self.order_items = []

    def add_item(self, item_name, quantity):
        """Add a menu item to the order.
        Parameters: item_name (str): The name of the item.
            quantity (int): The number of items to add.
        Returns:  None"""
        pass

    def remove_item(self, item_name):
        """Remove an item from the order.
         Parameters: item_name (str): The name of the item to remove.
        Returns: None"""
        pass

    def calculate_total(self):
        """Calculate the total cost of all ordered items.
        Returns: float: The total price."""
        pass


class Receipt:
    """Represents the final order receipt.
    Attributes: order (Order): The order associated with this receipt.
    Key Methods: generate_receipt(): Create a formatted receipt string.
        save_receipt(file_name): Save the receipt to a file."""
    def __init__(self, order):
        """Initialize a receipt with a given order.
        Parameters order : The completed order."""
        self.order = order

    def generate_receipt(self):
        """Generate a formatted text receipt and 
        Returns the receipt """
        pass

    def save_receipt(self, file_name):
        """ Save the generated receipt to a file."""
        pass


def main():
    """Main function to run the restaurant game.
    Purpose is to control game flow and show menu, take orders, and display the receipt.
     Returns None"""
    pass



main()
