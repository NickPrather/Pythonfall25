"""
Menu class for Restaurant Ordering Game
Handles menu loading and display functionality
"""
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
            for line in file:
                line = line.strip()
                if not line:  # skip empty lines
                    continue
                data = line.split(",")  # splits data with a comma
                category = data[0].strip()
                # Parse multiple items per line (format: Category, Size1, Price1, Size2, Price2, ...)
                i = 1
                while i < len(data):
                    size = data[i].strip()
                    name = f"{category} {size}"  # e.g., "Coke Large" for unique identification
                    price = float(data[i + 1].strip())
                    self.items.append((category, name, price))
                    i += 2
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

