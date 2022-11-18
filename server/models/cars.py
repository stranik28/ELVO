from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.base import Base

class Cars(Base):
    __tablename__ = "cars_table"
    id = Column(Integer, primary_key=True)
    number = Column(String(50))
    pts_hash = Column(String(50))
    verified = Column(Boolean)