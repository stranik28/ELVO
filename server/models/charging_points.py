from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.sql import func
from database.base import Base

class ChargingPoints(Base):
    __tablename__ = "charging_points"
    id = Column(Integer, primary_key=True)
    address = Column(String(50))
    types_of_charging = Column(ARRAY(Integer))
    coordinates = Column(String(50))
    number_of_places = Column(Integer)
    available_count = Column(Integer)
    cost = Column(Integer)
    company_id = Column(Integer)



    