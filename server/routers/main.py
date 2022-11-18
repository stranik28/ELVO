from fastapi import FastAPI, Request, APIRouter, Depends
from services.test import get_test_service

router = APIRouter(prefix="/test")

@router.get("/")
async def test(test=Depends(get_test_service)):
    return test.get_test()