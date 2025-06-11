from sqlalchemy import Column, Integer, String, DateTime
from app.db.base_class import Base
from datetime import datetime

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    people_count = Column(Integer, nullable=False)
    reserved_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)