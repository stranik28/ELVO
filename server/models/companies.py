from sqlalchemy import Column, Integer, String, FLOAT
from database.base import Base

class Companies(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    amount = Column(FLOAT)