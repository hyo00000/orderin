from pydantic import BaseModel
from typing import Optional

class MenuBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: int

class MenuCreate(MenuBase):
    pass

class MenuUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    is_available: Optional[int] = None

class MenuOut(MenuBase):
    id: int
    is_available: int

    class Config:
        orm_mode = True
