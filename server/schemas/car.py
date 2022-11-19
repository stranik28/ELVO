from pydantic import BaseModel

class Car(BaseModel):
    number: str
    pts_hash: str
    pts_number: str

class CarInDB(Car):
    id: int
    verified: bool
    denied: bool