from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.base import Base

class goods(Base):
    __tablename__ = "goods_table"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Integer)
    description = Column(String)
    hash = Column(String)
    partner_id = Column(Integer)