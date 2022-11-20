from repository.base import BaseRepository
from models.admin import admin as adminDb
from schemas.admin import Admin
from fastapi import HTTPException
from models.requests import requests
from models.users import users
from models.cars import Cars as CarInDB
from passlib.hash import pbkdf2_sha256


pwd_context = pbkdf2_sha256
pwd_context.using(salt="123".encode('utf-8'))
class AdminRepository(BaseRepository):
    def get_admins(self):
        return self.session.query(adminDb).all()

    def create_admin(self, admin: Admin):
        admin = admin.dict(exclude_unset=True)
        adminToDb = adminDb(
            login=admin["login"],
            hashed_password=pwd_context.hash(admin["password"])
        )
        self.session.add(adminToDb)
        self.session.commit()
        return adminToDb.id

    def get_admin_by_id(self, id: int):
        admin = self.session.query(adminDb).filter(adminDb.id == id).first()
        return admin

    def update_admin(self, id: int, admin: Admin):
        admin_in_db = self.session.query(adminDb).filter(adminDb.id == id).first()
        setattr(admin_in_db, 'login', admin.login)
        setattr(admin_in_db, 'hashed_password', pwd_context.hash(admin.password))
        self.session.commit()
        self.session.refresh(admin_in_db)
        return admin_in_db
    
    def get_requests(self):
        return self.session.query(requests).all()
    
    def approve_request(self, id: int):
        request = self.session.query(requests).filter(requests.id == id).first()
        car = self.session.query(CarInDB).filter(CarInDB.id == request.car_id).first()
        setattr(car, 'verified', False)
        setattr(request, 'status', 1)
        self.session.commit()
        self.session.refresh(request)
        return request
    
    def decline_request(self, id: int):
        request = self.session.query(requests).filter(requests.id == id).first()
        setattr(request, 'status', 2)
        car = self.session.query(CarInDB).filter(CarInDB.id == request.car_id).first()
        setattr(car, 'verified', False)
        self.session.add(car)
        self.session.commit()
        self.session.refresh(request)
        return request
    
    def delete_request(self, id: int):
        request = self.session.query(requests).filter(requests.id == id).first()
        car = self.session.query(CarInDB).filter(CarInDB.id == request.car_id).first()
        self.session.delete(request)
        self.session.commit()
        return request
    
    def get_requests_by_id(self, id: int):
        request = self.session.query(requests).filter(requests.id == id).first()
        car = self.session.query(CarInDB).filter(CarInDB.id == request.car_id).first()
        user = self.session.query(users).filter(users.id == request.user_id).first()
        sts = self.session.query(CarInDB).filter(CarInDB.id == car.sts_id).first()
        pts = self.session.query(CarInDB).filter(CarInDB.id == car.pts_id).first()
        return request, car, user, sts, pts
    

