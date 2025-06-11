from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    reservation_id = Column(Integer, ForeignKey("reservations.id", ondelete="SET NULL"), nullable=True)
    menu_id = Column(Integer, ForeignKey("menus.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    status = Column(String, default="pending")  # pending, preparing, completed
    ordered_at = Column(DateTime, default=datetime.utcnow)

    reservation = relationship("Reservation", backref="orders")
    menu = relationship("Menu")