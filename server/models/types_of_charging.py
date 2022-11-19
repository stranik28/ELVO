from sqlalchemy import Column, Integer, String
from database.base import Base

class TypesOfCharging(Base):
    __tablename__ = "types_of_charging"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))