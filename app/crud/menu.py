# app/crud/menu.py

from sqlalchemy.orm import Session
from app.models.menu import Menu
from app.schemas.menu import MenuCreate, MenuUpdate

def get_menu_list(db: Session):
    return db.query(Menu).all()

def get_menu(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()

def create_menu(db: Session, menu_in: MenuCreate):
    db_menu = Menu(**menu_in.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def update_menu(db: Session, db_menu: Menu, menu_in: MenuUpdate):
    for field, value in menu_in.dict(exclude_unset=True).items():
        setattr(db_menu, field, value)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def delete_menu(db: Session, db_menu: Menu):
    db.delete(db_menu)
    db.commit()
