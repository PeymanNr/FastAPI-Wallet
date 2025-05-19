from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from schemas.transaction import TransactionCreate, TransactionOut
from crud.transactions import create_transaction

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/", response_model=TransactionOut)
async def create(transaction: TransactionCreate, db: AsyncSession = Depends(get_db)):
    return await create_transaction(db, transaction)
