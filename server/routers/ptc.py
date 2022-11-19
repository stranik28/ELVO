from fastapi import APIRouter, Depends, HTTPException, status
from services.ptc import get_ptc_service
from repository.ptc import PTCRepository

router = APIRouter(prefix="/ptc", tags=["ptc"])

@router.get("/validate")
async def validate_ptc(service: PTCRepository = Depends(get_ptc_service)):
    return service.validate_ptc()

@router.get("/{ptc_id}")
async def get_ptc(ptc_id: int, service: PTCRepository = Depends(get_ptc_service)):
    ptc = service.get_ptc_by_id(ptc_id)
    if not ptc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PTC not found")
    return ptc

@router.post("/validate")
async def validate_ptc(ptc: int, service: PTCRepository = Depends(get_ptc_service)):
    return service.validate_ptc(ptc)