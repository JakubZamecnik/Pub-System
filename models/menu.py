from typing import List, Dict

class MenuItem:
    def __init__(self, item_id: str, name: str, price: float):
        self.item_id = item_id  # Např. "pivo_05"
        self.name = name
        self.price = price
