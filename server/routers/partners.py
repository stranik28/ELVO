from fastapi import APIRouter, Depends, HTTPException, status
from services.partner import get_partners_service
from schemas.partners import PartnerInDB, Partner
from datetime import datetime

router = APIRouter(prefix="/partners", tags=["partners"])

@router.get("/actual")
async def get_actual_partners(partners_service: get_partners_service = Depends()):
    return partners_service.get_actual_partners()
    # return "Not implemented"

@router.get("/")
async def get_partners(partners_service: get_partners_service = Depends()):
    return partners_service.get_partners()

@router.get("/{id}")
async def get_partner_by_id(id: int, partners_service: get_partners_service = Depends()):
    partner = partners_service.get_partner_by_id(id)
    if not partner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Partner not found")
    return partner

@router.post("/")
async def create_partner(partner: Partner, partners_service: get_partners_service = Depends()):
    return partners_service.create_partner(partner)

@router.put("/{id}")
async def update_partner(id: int, partner: Partner, partners_service: get_partners_service = Depends()):
    partner_in_db = partners_service.get_partner_by_id(id)
    if not partner_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Partner not found")
    partner_in_db = PartnerInDB(**partner.dict())
    return partners_service.update_partner(id, partner_in_db)

@router.delete("/{id}")
async def delete_partner(id: int, partners_service: get_partners_service = Depends()):
    partner_in_db = partners_service.get_partner_by_id(id)
    if not partner_in_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Partner not found")
    return partners_service.delete_partner(id)

@router.get("/category/{category}")
async def get_partners_by_category(category: str, partners_service: get_partners_service = Depends()):
    return partners_service.get_partners_by_category(category)

@router.get("/update_date/{update_date}")
async def get_partners_by_update_date(update_date: datetime, partners_service: get_partners_service = Depends()):
    return partners_service.get_partners_by_update_date(update_date)
