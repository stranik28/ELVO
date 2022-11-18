from sqlalchemy import Column, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from database.base import Base

class ChargingPoints(Base):
    __tablename__ = "charging_points"
    id = Column(Integer, primary_key=True)
    address = Column(String(50))
    latitude = Column(String(50))
    longitude = Column(String(50))
    number_of_places = Column(Integer)
    available_count = Column(Integer)
    cost = Column(Integer)
    types_of_charging = Column(ARRAY(Integer))
    company_id = Column(Integer)



    