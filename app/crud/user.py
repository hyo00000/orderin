# app/crud/admin.py

from sqlalchemy.orm import Session
from app.models.admin import Admin
from app.schemas.admin import AdminCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_admin_by_username(db: Session, username: str):
    return db.query(Admin).filter(Admin.username == username).first()

def create_admin(db: Session, admin_in: AdminCreate):
    hashed_pw = pwd_context.hash(admin_in.password)
    db_admin = Admin(username=admin_in.username, hashed_password=hashed_pw)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin
