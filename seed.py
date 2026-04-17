from app import app, db, MenuItem, Inventory, Table, Bank

def seed_database():
    with app.app_context():
        # 1. Vyčištění databáze (volitelné, pokud chceš začít znovu)
        db.drop_all()
        db.create_all()

        # 2. Inicializace banky (počáteční kapitál)
        startovni_hotovost = Bank(balance=1000.0)
        db.session.add(startovni_hotovost)

        # 3. Vytvoření položek menu
        pivo = MenuItem(name="Plzeň 12°", price=55.0, category="Nápoje")
        kofola = MenuItem(name="Kofola", price=35.0, category="Nápoje")
        burger = MenuItem(name="Hospodský Burger", price=185.0, category="Jídlo")
        
        db.session.add_all([pivo, kofola, burger])
        db.session.commit() # Commitneme, abychom získali ID pro sklad

        # 4. Naplnění skladu (propojujeme s ID v MenuItem)
        sklad_pivo = Inventory(menu_item_id=pivo.id, quantity=50)
        sklad_kofola = Inventory(menu_item_id=kofola.id, quantity=100)
        sklad_burger = Inventory(menu_item_id=burger.id, quantity=20)

        db.session.add_all([sklad_pivo, sklad_kofola, sklad_burger])

        # 5. Vytvoření stolů
        stoly = [
            Table(table_number=1, capacity=4),
            Table(table_number=2, capacity=2),
            Table(table_number=3, capacity=6)
        ]
        db.session.add_all(stoly)

        db.session.commit()
        print("Databáze byla úspěšně naplněna daty (Seed complete)!")

if __name__ == "__main__":
    seed_database()
