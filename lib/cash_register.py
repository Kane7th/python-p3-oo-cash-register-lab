class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.items = []  # Just item titles
        self.total = 0
        self._item_details = []  # Stores (title, price, quantity) for calculating total

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)  # Adds titles to items list
        self._item_details.append((title, price, quantity))  # Stores item details
        self.total += price * quantity  # Updates total with price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self._item_details:
            # Get the last transaction
            title, price, quantity = self._item_details.pop()
            
            # Remove all instances of that item from the items list
            for _ in range(quantity):
                self.items.pop()  # Remove the last item added
            
            # Subtract the corresponding total amount for that transaction
            self.total -= price * quantity

            # Reset total to 0.0 if all items have been removed
            if not self.items:
                self.total = 0.0
