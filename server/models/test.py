from sqlalchemy import Column, Integer, String
from database.base import Base

class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))