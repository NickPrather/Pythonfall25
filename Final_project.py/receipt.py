"""
Receipt class for Restaurant Ordering Game
Generates and saves order receipts
"""
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

