from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.base import Base

class Companies(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))