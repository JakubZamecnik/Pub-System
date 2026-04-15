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
