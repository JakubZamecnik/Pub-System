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