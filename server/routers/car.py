from fastapi import APIRouter, Depends, HTTPException
from schemas.car import Car, CarInDB
from services.car import get_car_service

router = APIRouter(prefix="/car", tags=["car"])

@router.get("/")
async def get_cars(car_service: get_car_service = Depends()):
    return car_service.get_cars()

@router.get("/{id}")
async def get_car(id: int, car_service: get_car_service = Depends()):
    return car_service.get_car_by_id(id)

@router.post("/")
async def create_car(car: Car,user_id:int, car_service: get_car_service = Depends()):
    return car_service.create_car(user_id,car)

@router.put("/{id}")
async def update_car(id: int, car: Car, car_service: get_car_service = Depends()):
    return car_service.update_car(id, car)

@router.delete("/{id}")
async def delete_car(id: int, car_service: get_car_service = Depends()):
    return car_service.delete_car(id)

@router.put("/status/{id}")
async def verify_car(id: int,status:bool, car_service: get_car_service = Depends()):
    return car_service.car_status(id, status)