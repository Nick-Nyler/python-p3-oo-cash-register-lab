#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []  # Store flat list of item names
        self.last_transaction = 0
        self.discount = discount
        self._item_details = []  # Store details for voiding and calculations

    def add_item(self, name, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        # Add item names to flat list
        for _ in range(quantity):
            self.items.append(name)
        # Store details for voiding
        self._item_details.append({"name": name, "price": price, "quantity": quantity, "cost": item_cost})
        self.last_transaction = item_cost

    def apply_discount(self):
        if self.discount <= 0:
            print("There is no discount to apply.")
            return
        discount_amount = (self.discount / 100.0) * self.total
        self.total -= discount_amount
        formatted_total = int(self.total) if self.total.is_integer() else self.total
        print(f"After the discount, the total comes to ${formatted_total}.")

    def get_total(self):
        return self.total

    def void_last_transaction(self):
        if self._item_details:
            last_item = self._item_details.pop()
            self.total -= last_item["cost"]
            self.last_transaction = -last_item["cost"]
            # Remove the last `quantity` items with the same name
            for _ in range(last_item["quantity"]):
                if self.items and self.items[-1] == last_item["name"]:
                    self.items.pop()
        else:
            self.last_transaction = 0

    def get_items(self):
        return self.items  # Return the flat list directly