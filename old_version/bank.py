class Bank:
    def __init__(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def add_money(self, amount: float):
        self.balance += amount
        print(f"BANKA: Přijata platba {amount} Kč. Aktuální stav kasy: {self.balance} Kč.")
