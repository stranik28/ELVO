from repository.base import BaseRepository
from schemas.charging_points import ChargingPoint
from models.charging_points import ChargingPoints as ChargingPointInDB

class ChargingPointsRepository(BaseRepository):
    def get_charging_points(self):
        return self.session.query(ChargingPointInDB).all()

    def create_charging_point(self, charging_point: ChargingPoint):
        charging_point_in_db = ChargingPointInDB(**charging_point.dict())
        self.session.add(charging_point_in_db)
        self.session.commit()
        self.session.refresh(charging_point_in_db)
        return charging_point_in_db

    def get_charging_point_by_id(self, id: int):
        return self.session.query(ChargingPointInDB).filter(ChargingPointInDB.id == id).first()

    def update_charging_point(self, id: int, charging_point: ChargingPoint):
        charging_point_in_db = self.session.query(ChargingPointInDB).filter(ChargingPointInDB.id == id).first()
        charging_point_in_db.adress = charging_point.adress
        charging_point_in_db.types_of_charging_points = charging_point.types_of_charging_points
        charging_point_in_db.number_of_charging_points = charging_point.number_of_charging_points
        charging_point_in_db.avaliable_count = charging_point.avaliable_count
        charging_point_in_db.cost = charging_point.cost
        charging_point_in_db.company_id = charging_point.company_id
        self.session.commit()
        return charging_point_in_db

    def delete_charging_point(self, id: int):
        charging_point_in_db = self.session.query(ChargingPointInDB).filter(ChargingPointInDB.id == id).first()
        self.session.delete(charging_point_in_db)
        self.session.commit()
        return charging_point_in_db
