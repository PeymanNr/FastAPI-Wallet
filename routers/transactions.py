from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from db.database import get_db
from schemas.transaction import TransactionCreateSchema, TransactionOutSchema
from crud.transactions import create_transaction, get_transactions


router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionOutSchema)
async def create(transaction: TransactionCreateSchema, db: AsyncSession = Depends(get_db)):
    return await create_transaction(db, transaction)


@router.get("/", response_model=List[TransactionOutSchema])
async def list_transactions(
    type: Optional[str] = Query(default=None, description="Filter by type: income or expense"),
    sort: str = Query(default="desc", description="Sort by date: asc or desc"),
    db: AsyncSession = Depends(get_db)
):
    return await get_transactions(db, type=type, sort=sort)

