from repository.charging_points import ChargingPointsRepository
from database.connections import get_database_connection

def get_charging_points_service() -> ChargingPointsRepository:
    db = get_database_connection()
    return ChargingPointsRepository(next(db))