from fastapi import APIRouter, Depends
from schemas.charging_points import ChargingPoint
from services.charging_points import get_charging_points_service

router = APIRouter(prefix="/charging_points", tags=["charging_points"])

@router.get("/")
async def get_charging_points(
    charging_point_service: get_charging_points_service = Depends()
):
    return charging_point_service.get_charging_points()

@router.get("/{id}")
async def get_charging_point(
    id: int,
    charging_point_service: get_charging_points_service = Depends()
):
    return charging_point_service.get_charging_point(id)

@router.post("/")
async def create_charging_point(
    charging_point: ChargingPoint,
    charging_point_service: get_charging_points_service = Depends()
):
    return charging_point_service.create_charging_point(charging_point)

@router.put("/{id}")
async def update_charging_point(
    id: int,
    charging_point: ChargingPoint,
    charging_point_service: get_charging_points_service = Depends()
):
    return charging_point_service.update_charging_point(id, charging_point)

@router.delete("/{id}")
async def delete_charging_point(
    id: int,
    charging_point_service: get_charging_points_service = Depends()
):
    return charging_point_service.delete_charging_point(id)


