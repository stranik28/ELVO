from pydantic import BaseModel
from datetime import datetime

class Partner(BaseModel):
    name: str
    address: str
    category: str
    body: str
    date: datetime

class PartnerInDB(Partner):
    id: int