# app/crud/reservation.py

from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from app.schemas.reservation import ReservationCreate

def get_reservations(db: Session):
    return db.query(Reservation).order_by(Reservation.reserved_at).all()

def get_reservation(db: Session, reservation_id: int):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def create_reservation(db: Session, reservation_in: ReservationCreate):
    db_reservation = Reservation(**reservation_in.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation
