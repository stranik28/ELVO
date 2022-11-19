from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.base import Base
from models.ptses import pts
from models.sts import sts

class Cars(Base):
    __tablename__ = "cars_table"
    id = Column(Integer, primary_key=True)
    sts_id = Column(Integer)
    pts_id = Column(Integer)
    verified = Column(Boolean)