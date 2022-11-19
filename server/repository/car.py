from repository.base import BaseRepository
from schemas.car import Car
from models.cars import Cars as CarInDB

class CarRepository(BaseRepository):
    def get_cars(self):
        return self.session.query(CarInDB).all()

    def create_car(self, car: Car):
        car_in_db = CarInDB(**car.dict())
        self.session.add(car_in_db)
        self.session.commit()
        self.session.refresh(car_in_db)
        return car_in_db

    def get_car_by_id(self, id: int):
        return self.session.query(CarInDB).filter(CarInDB.id == id).first()

    def update_car(self, id: int, car: Car):
        car_in_db = self.session.query(CarInDB).filter(CarInDB.id == id).first()
        car_in_db.number = car.number
        car_in_db.pts_hash = car.pts_hash
        car_in_db.verified = car.verified
        car_in_db.denied = car.denied
        self.session.commit()
        return car_in_db

    def delete_car(self, id: int):
        car_in_db = self.session.query(CarInDB).filter(CarInDB.id == id).first()
        self.session.delete(car_in_db)
        self.session.commit()
        return car_in_db

    def verify_car(self, id: int, verified: bool):
        car_in_db = self.session.query(CarInDB).filter(CarInDB.id == id).first()
        car_in_db.verified = True
        car_in_db.denied = verified
        self.session.commit()
        return car_in_db

    def car_car_to_verify(self, id: int):
        car_in_db = self.session.query(CarInDB).filter(CarInDB.verified == False).all()
        return car_in_db

    