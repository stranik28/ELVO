from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from database.base import Base

class QrCodes(Base):
    __tablename__ = "qr_table"
    id = Column(Integer, primary_key=True)
    hash = Column(String(128))
    created_at = Column(DateTime(timezone=True), server_default=func.now())