from pydantic import BaseModel

class Car(BaseModel):
    vin_pts: str
    auto_model: str
    body_color: str
    engine_type: str
    pts_hash: str

    vin_sts: str
    number: str
    sts_hash: str

class CarInDB(Car):
    id: int
    verified: bool
    denied: bool