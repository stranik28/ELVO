from schemas.transactions import TransactionBaseSchema, TransactionSchema
from services.transactions import get_transaction_service
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)

@router.get("/")
async def get_transactions():
    return get_transaction_service().get_transactions()

@router.get("/{id}")
async def get_transaction(id: int):
    transaction = get_transaction_service().get_transaction(id)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    return transaction

@router.post("/")
async def create_transaction(transaction: TransactionBaseSchema):
    return get_transaction_service().create_transaction(transaction)

@router.put("/{id}")
async def update_transaction(id: int, transaction: TransactionBaseSchema):
    return get_transaction_service().update_transaction(id, transaction)

@router.delete("/{id}")
async def delete_transaction(id: int):
    return get_transaction_service().delete_transaction(id)

# Path: server/routers/users.py
