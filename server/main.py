from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from routers.charging_points import router as charging_points_router
from routers.users import router as user_router
from routers.reviews import router as reviews_router
from routers.car import router as car_router
from routers.transactions import router as transactions_router
from routers.companies import router as companies_router
from routers.partners import router as partners_router

app = FastAPI(
    title="FastAPI",
    description="FastAPI",
    version="0.1.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

app.include_router(charging_points_router)
app.include_router(user_router)
app.include_router(reviews_router)
app.include_router(car_router)
app.include_router(transactions_router)
app.include_router(companies_router)
app.include_router(partners_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)