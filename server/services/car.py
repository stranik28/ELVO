from repository.car import CarRepository
from database.connections import get_database_connection

def get_car_service() -> CarRepository:
    db = get_database_connection()
    return CarRepository(next(db))