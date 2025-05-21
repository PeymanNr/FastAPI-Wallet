from fastapi import APIRouter, Depends, Query
from schemas.report import BalanceReportSchema
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from crud.reports import get_balance

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/balance", response_model=BalanceReportSchema)
async def get_transaction_balance(db: AsyncSession = Depends(get_db)):
    return await get_balance(db)