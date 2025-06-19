# app/crud/order.py

from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate

def get_orders(db: Session):
    return db.query(Order).order_by(Order.ordered_at.desc()).all()

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def create_order(db: Session, order_in: OrderCreate):
    db_order = Order(**order_in.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order_status(db: Session, db_order: Order, order_in: OrderUpdate):
    db_order.status = order_in.status
    db.commit()
    db.refresh(db_order)
    return db_order
