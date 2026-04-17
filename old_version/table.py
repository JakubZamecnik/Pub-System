from typing import List
from .guest import Guest

class Table:
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.guests: List[Guest] = []

    def add_guest(self, guest: Guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            print("Stůl je plný!")

    def remove_guest(self, guest: Guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def get_guest_names(self) -> List[str]:
        return [guest.name for guest in self.guests]

    def get_total_bill(self) -> float:
        return sum(guest.get_total() for guest in self.guests)

    def is_table_clear(self) -> bool:
        """Vrátí True, pokud všichni hosté u stolu zaplatili."""
        if not self.guests:
            return True
        return all(guest.is_paid for guest in self.guests)

    def checkout_table(self):
        """Pokud je zaplaceno, vyndá všechny hosty a stůl je volný."""
        if self.is_table_clear():
            self.guests = []
            print(f"Stůl č. {self.table_number} je nyní volný.")
        else:
            print(f"U stolu č. {self.table_number} ještě někdo dluží!")
    