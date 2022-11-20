from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.base import Base

class category(Base):
    __tablename__ = "category_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)