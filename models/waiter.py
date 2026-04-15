from .guest import Guest
from .menu import MenuItem

class Waiter:
    def __init__(self, name: str):
        self.name = name

    def serve_item(self, guest: Guest, item: MenuItem, inventory: Inventory):
        if inventory.check_and_reduce(item.name):
            guest.add_order(item)
            print(f"Číšník přinesl {item.name}.")
        else:
            print(f"Bohužel, {item.name} už došlo!")


    def clear_guest_bill(self, guest: Guest):
        """Pomocná metoda pro zaplacení (příprava pro budoucí kasu)."""
        total = guest.get_total()
        print(f"Host {guest.name} platí {total} Kč.")
        guest.is_paid = True
