from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from database.base import Base

class requests(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    car_id = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
