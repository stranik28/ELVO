from fastapi import APIRouter, Depends
from schemas.companies import Company
from services.companies import get_companies_service

router = APIRouter(prefix="/companies", tags=["companies"])

@router.get("/")
async def get_companies(
    companies_service: get_companies_service = Depends()
):
    return companies_service.get_companies()

@router.get("/{id}")
async def get_company(
    id: int,
    companies_service: get_companies_service = Depends()
):
    return companies_service.get_company_by_id(id)

@router.post("/")
async def create_company(
    company: Company,
    companies_service: get_companies_service = Depends()
):
    return companies_service.create_company(company)

@router.put("/{id}")
async def update_company(
    id: int,
    company: Company,
    companies_service: get_companies_service = Depends()
):
    return companies_service.update_company(id, company)

@router.delete("/{id}")
async def delete_company(
    id: int,
    companies_service: get_companies_service = Depends()
):
    return companies_service.delete_company(id)