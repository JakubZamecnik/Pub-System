from typing import List, Dict
from .menu import MenuItem

class Inventory:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_stock(self, menu_item: MenuItem, quantity: int):
        """Přidá zboží na sklad nebo navýší počet. Propojeno přes item_id."""
        item_id = menu_item.item_id
        if item_id in self.items:
            self.items[item_id] += quantity
        else:
            self.items[item_id] = quantity
        print(f"Sklad: Přidáno {quantity}x {menu_item.name} (ID: {item_id}). Celkem: {self.items[item_id]}")

    def check_and_reduce(self, menu_item: MenuItem) -> bool:
        """Zkontroluje sklad podle item_id a odebere 1 ks, pokud je skladem."""
        item_id = menu_item.item_id
        if item_id in self.items and self.items[item_id] > 0:
            self.items[item_id] -= 1
            return True
        return False

    def get_status(self):
        return self.items
