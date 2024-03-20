#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []
    
   

    def add_item(self, title, price, quantity = 1):
        one_item = price * quantity
        self.title = title
        self.total += one_item
        for i in range(quantity):
            self.items.append(title)
        self.transactions.append([title, one_item])

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total *= (1- self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total -= (self.transactions[-1][-1])
        self.transactions.pop()
