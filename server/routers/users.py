from fastapi import FastAPI, Request, APIRouter, Depends
from services.user import get_user_service
from schemas.user import UserBaseSchema
from pydantic_partial import create_partial_model

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def get_users(request: Request, user_service: get_user_service = Depends()):
    return user_service.get_all()

@router.get("/{id}")
async def get_user_by_id(request: Request, id: int, user_service: get_user_service = Depends()):
    return user_service.get_user_by_id(id)

@router.post("/")
async def create_user(request: Request, user: UserBaseSchema, user_service: get_user_service = Depends()):
    return user_service.create_user(user)

@router.put("/{id}")
async def update_user(request: Request, id: int, user: UserBaseSchema, user_service: get_user_service = Depends()):
    return user_service.update_user(id, user)

@router.delete("/{id}")
async def delete_user(request: Request, id: int, user_service: get_user_service = Depends()):
    return user_service.delete_user(id)

@router.patch("/{id}")
async def patch_user(request: Request, id: int, user: create_partial_model(UserBaseSchema), user_service: get_user_service = Depends()):
    return user_service.patch_user(id, user)



