"""
Order class for Restaurant Ordering Game
Tracks user's order items and calculates totals
"""
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

