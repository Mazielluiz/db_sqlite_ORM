from __future__ import annotations

from sqlalchemy.orm import Session

from config.base import Base, engine
from config.settings import DEFAULT_USER
from models.customer import Customer
from models.order import Order

def create_db() -> None:
    Base.metadata.create_all(engine)

def drop_db() -> None:
    Base.metadata.drop_all(engine)

def create_customer(session: Session, name: str, email: str) -> Customer:
    C = Customer(name=name, email=email)
    session.add(C)
    session.flush()
    return C

def create_order(session: Session, customer_id: int, item: str, price: float) -> Order:
    O = Order(customer_id=customer_id, item=item, price=price)
    session.add(O)
    session.flush()
    return O

def main():
    drop_db()
    create_db()

    with Session(engine) as session:
        print("\n=== Criando cliente ===")
        customer = create_customer(session, DEFAULT_USER["name"], DEFAULT_USER["email"])
        print(f"✓ Cliente criado: {customer}\n")

        print("=== Criando pedidos ===")
        order1 = create_order(session, customer.id, "Laptop", 2500.00)
        order2 = create_order(session, customer.id, "Mouse", 50.00)
        order3 = create_order(session, customer.id, "Teclado Gamer", 50.00)
        order4 = create_order(session, customer.id, "Celular", 3000.00)

        print(f"✓ Pedido 1: {order1}")
        print(f"✓ Pedido 2: {order2}")
        print(f"✓ Pedido 3: {order3}")
        print(f"✓ Pedido 4: {order4}")

        session.commit()

        print("=== Consultando dados ===")
        customers = session.query(Customer).all()
        print(f"Todos os Clientes:")
        for c in customers:
            print(f"  • {c}")

        customers_orders = session.query(Order).filter(Order.customer_id == customer.id).all()
        print(f"\nPedidos do Cliente {customer.name}:")
        for o in customers_orders:
            print(f"  • {o}")
        print()

if __name__ == "__main__":
    main()