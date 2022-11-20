from fastapi import APIRouter, Depends, HTTPException, status
from services.goods import get_goods_service
from schemas.goods import Goods
from models.goods import GoodsInDB

router = APIRouter(prefix="/goods", tags=["goods"])

@router.get("/")
async def get_goods(goods_service: get_goods_service = Depends()):
    return goods_service.get_goods()

@router.get("/{id}")
async def get_goods_by_id(id: int, goods_service: get_goods_service = Depends()):
    goods = goods_service.get_goods_by_id(id)
    if not goods:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goods not found")
    return goods

@router.post("/")
async def create_goods(goods: Goods, goods_service: get_goods_service = Depends()):
    return goods_service.create_goods(goods)

@router.put("/{id}")
async def update_goods(id: int, goods: Goods, goods_service: get_goods_service = Depends()):
    goods_in_db = goods_service.get_goods_by_id(id)
    if not goods_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goods not found")
    goods_in_db = GoodsInDB(**goods.dict())
    return goods_service.update_goods(id, goods_in_db)

@router.delete("/{id}")
async def delete_goods(id: int, goods_service: get_goods_service = Depends()):
    goods_in_db = goods_service.get_goods_by_id(id)
    if not goods_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goods not found")
    return goods_service.delete_goods(id)



