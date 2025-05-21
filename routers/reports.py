from fastapi import APIRouter, Depends, Query
from schemas.report import BalanceReportSchema, ReportByDateTimeSchema
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from crud.reports import get_balance, get_report_by_datetime
from typing import List

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/balance", response_model=BalanceReportSchema)
async def get_transaction_balance(db: AsyncSession = Depends(get_db)):
    return await get_balance(db)

@router.get("/detailed/", response_model=List[ReportByDateTimeSchema])
async def detailed_report(db: AsyncSession = Depends(get_db)):
    return await get_report_by_datetime(db)
