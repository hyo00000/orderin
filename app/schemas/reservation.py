from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReservationBase(BaseModel):
    customer_name: str
    phone: Optional[str] = None
    people_count: int
    reserved_at: datetime

class ReservationCreate(ReservationBase):
    pass

class ReservationOut(ReservationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
