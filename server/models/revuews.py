from sqlalchemy import Column, Integer, String, DateTime, FLOAT
from sqlalchemy.sql import func
from database.base import Base

class Revuews(Base):
    __tablename__ = "revuews"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    charging_point_id = Column(Integer)
    body = Column(String(50))
    stars = Column(FLOAT)
    date = Column(DateTime(timezone=True), server_default=func.now())