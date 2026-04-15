from typing import List, Dict

class Inventory:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_stock(self, item: str, quantity: int):
        """Přidá zboží na sklad nebo navýší počet."""
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity
        print(f"Sklad: Přidáno {quantity}x {name}. Celkem: {self.items[name]}")

    def check_and_reduce(self, name: str) -> bool:
        """Zkontroluje, zda je jídlo skladem, a pokud ano, odebere 1 kus."""
        if name in self.items and self.items[name] > 0:
            self.items[name] -= 1
            return True
        return False

    def get_status(self):
        return self.items    
    