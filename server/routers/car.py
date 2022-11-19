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
async def create_car(car: Car, car_service: get_car_service = Depends()):
    return car_service.create_car(car)

@router.put("/{id}")
async def update_car(id: int, car: Car, car_service: get_car_service = Depends()):
    return car_service.update_car(id, car)

@router.delete("/{id}")
async def delete_car(id: int, car_service: get_car_service = Depends()):
    return car_service.delete_car(id)

@router.put("/verify/{id}")
async def verify_car(id: int, car_service: get_car_service = Depends()):
    return car_service.verify_car(id, False)

@router.put("/deny/{id}")
async def deny_car(id: int, car_service: get_car_service = Depends()):
    return car_service.verify_car(id, True)

@router.get("/to_verify")
async def car_to_verify(car_service: get_car_service = Depends()):
    return car_service.car_to_verify()

@router.get("/fast_verify/{number}")
async def fast_verify(number: str, car_service: get_car_service = Depends()):
    return car_service.fast_verify(number)