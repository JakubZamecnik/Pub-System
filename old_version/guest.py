from typing import List
from .menu import MenuItem  # Tečka znamená "ze stejné složky"

class Guest:
    def __init__(self, name: str):
        self.name = name
        self.orders: List[MenuItem] = []
        self.is_paid = False

    def add_order(self, item: MenuItem):
        self.orders.append(item)

    def get_total(self) -> float:
        return sum(item.price for item in self.orders)

    def pay(self) -> float:
        """Vrátí celkovou částku k zaplacení a označí hosta za zaplaceného."""
        if self.is_paid:
            print(f"Host {self.name} už má zaplaceno.")
            return 0.0
        
        total = self.get_total()
        self.is_paid = True
        print(f"Host {self.name} zaplatil {total} Kč.")
        return total
    
