import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.menu import MenuItem
from models.guest import Guest
from models.inventory import Inventory
from models.waiter import Waiter

# 1. Menu a Sklad (nezapomeň na item_id!)
pivo = MenuItem(item_id="p1", name="Prazdroj 12°", price=65.0)
sklad = Inventory()
sklad.add_stock(pivo, 1) # Máme jen JEDNO pivo

# 2. Lidé
pepa = Waiter("Pepa")
jakub = Guest("Jakub")

# 3. Akce - zkusíme objednat dvě piva
print("--- První objednávka ---")
pepa.serve_item(jakub, pivo, sklad)

print("\n--- Druhá objednávka ---")
pepa.serve_item(jakub, pivo, sklad)

# 4. Výsledek
print(f"\nCelková útrata: {jakub.get_total()} Kč.")
