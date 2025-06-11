from sqlalchemy import Column, String, Integer
from app.db.base_class import Base

class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    is_available = Column(Integer, default=1) #판매중:1, 품절:0
