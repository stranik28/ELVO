from pydantic import BaseModel
from typing import List

class ChargingPoint(BaseModel):
    address: str # Address of charging
    types_of_charging: List[int] # Тип коннкетора
    number_of_places: int # КОличество зарядных мест
    available_count: int # Количество доступных зарядных мест
    cost: int # Стоимость зарядки
    company_id: int # ID компании

class ChargingPointInDB(ChargingPoint):
    id: int