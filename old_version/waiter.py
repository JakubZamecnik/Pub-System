from .guest import Guest
from .menu import MenuItem
from .inventory import Inventory
from .bank import Bank

class Waiter:
    def __init__(self, name: str):
        self.name = name

    def serve_item(self, guest: Guest, item: MenuItem, inventory: Inventory):
        if inventory.check_and_reduce(item):
            guest.add_order(item)
            print(f"Číšník {self.name} přinesl {item.name} hostovi {guest.name}.")
        else:
            print(f"Bohužel, {item.name} už došlo! Číšník {self.name} nemůže přinést.")


    def process_payment(self, guest: Guest, bank: Bank):
        """Číšník vybere peníze od hosta a vloží je do banky."""
        amount = guest.pay()
        if amount > 0:
            bank.add_money(amount)

        