from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.base import Base

class sts(Base):
    __tablename__ = "sts_table"
    id = Column(Integer, primary_key=True)
    image_hash = Column(String)
    vin = Column(String)
    number = Column(String)
    