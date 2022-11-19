from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.base import Base

class pts(Base):
    __tablename__ = "pts_table"
    id = Column(Integer, primary_key=True)
    image_hash = Column(String)
    vin = Column(String)
    auto_model = Column(String)
    body_color = Column(String)
    engine_type = Column(String)
    