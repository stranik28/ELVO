from fastapi import APIRouter, Depends, HTTPException
from schemas.admin import Admin
from services.admin import get_admin_service

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/")
async def get_admins(admin_service: get_admin_service = Depends()):
    return admin_service.get_admins()

@router.post("/")
async def create_admin(admin: Admin, admin_service: get_admin_service = Depends()):
    return admin_service.create_admin(admin)

@router.get("/{id}")
async def get_admin(id: int, admin_service: get_admin_service = Depends()):
    return admin_service.get_admin_by_id(id)

@router.put("/{id}")
async def update_admin(id: int, admin: Admin, admin_service: get_admin_service = Depends()):
    return admin_service.update_admin(id, admin)

@router.delete("/{id}")
async def delete_admin(id: int, admin_service: get_admin_service = Depends()):
    return admin_service.delete_admin(id)

@router.post("/get_requests")
async def get_requests(admin_service: get_admin_service = Depends()):
    return admin_service.get_requests()

@router.post("/approve_request")
async def accept_request(id: int, admin_service: get_admin_service = Depends()):
    return admin_service.approve_request(id)

@router.post("/deciline_request")
async def reject_request(id: int, admin_service: get_admin_service = Depends()):
    return admin_service.decline_request(id)

@router.get("/get_requests/{id}")
async def get_requests_by_id(id: int, admin_service: get_admin_service = Depends()):
    return admin_service.get_requests_by_id(id)