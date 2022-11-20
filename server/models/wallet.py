from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from database.base import Base

class wallet(Base):
    __tablename__ = "wallet_table"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    company_id = Column(Integer)
    balance = Column(Integer)