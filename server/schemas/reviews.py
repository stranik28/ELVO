from pydantic import BaseModel
from datetime import datetime


class Review(BaseModel):
    body: str
    stars: float
    charging_point_id: int
    user_id: int

class ReviewInDB(Review):
    id: int
    date: datetime