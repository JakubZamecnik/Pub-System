from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.db'
db = SQLAlchemy(app)

class MenuItem(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    category: Mapped[str] = mapped_column(db.String(100), nullable=False)

class Bank(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    balance: Mapped[float] = mapped_column(db.Float, default=0.0)

class Guest(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)
    is_paid: Mapped[bool] = mapped_column(db.Boolean, default=False)
    # Přidáme propojení ke stolu
    table_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('table.id'), nullable=True)

class Inventory(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    
    # 1. Cizí klíč: Propojí tenhle řádek skladu s ID v Menu
    menu_item_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    
    # 2. Relationship: Tohle je "zkratka" pro Python, abys mohl napsat inventory.item.name
    item: Mapped["MenuItem"] = relationship('MenuItem', backref='inventory_records')
    
    quantity: Mapped[int] = mapped_column(db.Integer, default=0)


class Waiter(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False)

class Table(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    table_number: Mapped[int] = mapped_column(db.Integer, nullable=False)
    capacity: Mapped[int] = mapped_column(db.Integer, nullable=False)
    # Opravený vztah k hostům
    guests: Mapped[List["Guest"]] = relationship('Guest', backref='table')

class Order(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    guest_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('guest.id'), nullable=False)
    menu_item_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    guest: Mapped["Guest"] = relationship('Guest', backref='orders')
    item: Mapped["MenuItem"] = relationship('MenuItem')



with app.app_context():
    db.create_all()

@app.route('/')
def home():
    vsechny_stoly = Table.query.all()
    return render_template('index.html', tables=vsechny_stoly)


@app.route('/objednat')
def objednat():

    pivo = MenuItem.query.first()
    host = Guest.query.first()
    if not host:
        host = Guest(name="Jakub")
        db.session.add(host)
        db.session.commit()

    sklad = Inventory.query.filter_by(menu_item_id=pivo.id).first()

    if sklad and sklad.quantity > 0:
        sklad.quantity -= 1
        nova_objednavka = Order(guest_id=host.id, menu_item_id=pivo.id)
        db.session.add(nova_objednavka)
        db.session.commit()
        return f"Hotovo! Host {host.name} dostal {pivo.name}. Na skladě zbývá {sklad.quantity} ks."
    else:
        return "Bohužel, pivo došlo!"



@app.route('/zaplatit/<int:guest_id>')
def zaplatit(guest_id):
    host = Guest.query.get_or_404(guest_id)
    
    # 1. Spočítáme celkovou sumu za všechny jeho objednávky
    # Využíváme backref 'orders', který jsme definovali v modelu Order
    celkova_suma = sum(order.item.price for order in host.orders)
    
    if celkova_suma > 0:
        # 2. Přičteme peníze do banky (předpokládáme, že v bance je vždy aspoň jeden záznam)
        banka = Bank.query.first()
        if not banka:
            banka = Bank(balance=0.0)
            db.session.add(banka)
        
        banka.balance += celkova_suma
        
        # 3. Smažeme objednávky hosta (už jsou zaplacené)
        for order in host.orders:
            db.session.delete(order)
        
        # 4. Host je nyní "čistý" - můžeme ho buď smazat, nebo mu nastavit is_paid=True
        host.is_paid = True 
        
        db.session.commit()
        return f"Host {host.name} zaplatil {celkova_suma} Kč. V bance je nyní {banka.balance} Kč."
    else:
        return f"Host {host.name} nemá nic ke placení."



if __name__ == "__main__":
    app.run(debug=True)
