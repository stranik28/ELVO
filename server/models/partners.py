from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database.base import Base

class Partners(Base):
    __tablename__ = "partners"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    address = Column(String(50))
    category = Column(String(50))
    body = Column(String(50))
    date = Column(DateTime(timezone=True), server_default=func.now())