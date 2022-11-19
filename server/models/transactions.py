from sqlalchemy import Column, Integer, String, DateTime, FLOAT
from sqlalchemy.sql import func
from database.base import Base

class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    company_id = Column(Integer)
    amount = Column(FLOAT)
    body = Column(String(50))
    date = Column(DateTime(timezone=True), server_default=func.now())