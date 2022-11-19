from repository.base import BaseRepository
from schemas.car import Car
from models.cars import Cars as CarInDB
from models.ptses import pts
from models.sts import sts
from fastapi import HTTPException
from models.requests import requests
from models.users import users

class CarRepository(BaseRepository):
    def get_cars(self):
        return self.session.query(CarInDB).all()

    def create_car(self,user_id, car: Car):
        user = self.session.query(users).filter(users.id == user_id).first()
        if(not user):
            raise HTTPException(status_code=404, detail="User not found")
        ptsInDB = self.session.query(pts).filter(pts.vin == car.vin_pts).first()
        stsInDB = self.session.query(sts).filter(sts.vin == car.vin_sts).first()
        if(ptsInDB or stsInDB):
            raise HTTPException(status_code=400, detail="Car already exists")
        if(car.vin_pts != car.vin_sts):
            raise HTTPException(status_code=400, detail="VIN numbers are not equal")
        ptstodb = pts(vin=car.vin_pts, image_hash=car.pts_hash, auto_model=car.auto_model, body_color=car.body_color, engine_type=car.engine_type)
        ststodb = sts(vin=car.vin_sts, image_hash=car.sts_hash, number=car.number)
        self.session.add(ptstodb)
        self.session.add(ststodb)
        self.session.commit()
        car_in_db = CarInDB(sts_id=ststodb.id, pts_id=ptstodb.id, verified=True)
        self.session.add(car_in_db)
        self.session.commit()
        # добавим юзеру в массив cars id машины
        cars = user.cars.copy()
        print(cars)
        print(car_in_db.id)
        cars.append(car_in_db.id)
        setattr(user, 'cars',cars)
        self.session.commit()
        print(user.cars)
        request = requests(user_id=user_id, car_id=car_in_db.id)
        self.session.add(request, user)
        self.session.commit()
        self.session.refresh(car_in_db)

        return car_in_db

    def get_car_by_id(self, id: int):
        car = self.session.query(CarInDB).filter(CarInDB.id == id).first()
        # get pts and sts
        ptsFromDb = self.session.query(pts).filter(pts.id == car.pts_id).first()
        stsFromDb = self.session.query(sts).filter(sts.id == car.sts_id).first()
        # return 3 objects
        return car, ptsFromDb, stsFromDb

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

    def car_status(self, id: int, status: bool):
        car_in_db = self.session.query(CarInDB).filter(CarInDB.id == id).first()
        if(not car_in_db):
            raise HTTPException(status_code=404, detail="Car not found")
        car_in_db.verified = status
        self.session.commit()
        return "Car status updated"

    