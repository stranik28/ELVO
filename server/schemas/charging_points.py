from pydantic import BaseModel
from typing import List

class ChargingPoint(BaseModel):
    adress: str # Address of charging
    types_of_charging_points: List[int] # Тип коннкетора
    number_of_charging_points: int # КОличество зарядных мест
    avaliable_count: int # Количество доступных зарядных мест
    cost: int # Стоимость зарядки
    company_id: int # ID компании

class ChargingPointInDB(ChargingPoint):
    id: int