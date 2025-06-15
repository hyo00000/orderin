from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    menu_id: int
    quantity: int = 1

class OrderCreate(OrderBase):
    reservation_id: Optional[int] = None  # 현장 주문은 없음

class OrderUpdate(BaseModel):
    status: str  # "preparing", "completed", 등

class OrderOut(OrderBase):
    id: int
    status: str
    ordered_at: datetime
    reservation_id: Optional[int] = None

    class Config:
        orm_mode = True
