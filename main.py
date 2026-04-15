import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.menu import MenuItem
from models.guest import Guest
from models.table import Table
from models.waiter import Waiter

# 1. Příprava menu
pivo = MenuItem("Prazdroj 12°", 65.0)
rizek = MenuItem("Kuřecí řízek", 185.0)

# 2. Příprava personálu a místa
pepa = Waiter("Pepa")
stul_1 = Table(table_number=1, capacity=4)

# 3. Hosté přicházejí
host1 = Guest("Jakub")
stul_1.add_guest(host1)

# 4. Objednáváme
pepa.serve_item(host1, pivo)
pepa.serve_item(host1, rizek)

# 5. Kontrola
print(f"Celková útrata hosta {host1.name}: {host1.get_total()} Kč.")
