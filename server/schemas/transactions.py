from pydantic import BaseModel
from datetime import datetime

class TransactionBaseSchema(BaseModel):
    user_id: int
    company_id: int
    amount: float
    body: str

class TransactionSchema(TransactionBaseSchema):
    id: int
    date: datetime