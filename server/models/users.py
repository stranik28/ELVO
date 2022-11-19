from sqlalchemy import Column, Integer, String, ForeignKey
from database.base import Base

class users(Base):
    __tablename__ = "users_table"
    id = Column(Integer, primary_key=True)
    fio = Column(String(255))
    login = Column(String(50))
    hashed_password = Column(String(50))
    email = Column(String(50))
    refresh_token = Column(String(50))
    cars = Column(Integer, ForeignKey('cars_table.id'))
    qr_id = Column(Integer, ForeignKey('qr_table.id'))
    card = Column(String(50))