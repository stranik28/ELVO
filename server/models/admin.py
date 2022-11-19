from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from database.base import Base

class Admin(Base):
    __tablename__ = "admin_table"
    id = Column(Integer, primary_key=True)
    login = Column(String(50))
    hashed_password = Column(String(128))