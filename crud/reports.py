from sqlalchemy import select, func, case
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Transaction
from schemas.report import ReportByDateTimeSchema



async def get_balance(
    db: AsyncSession,
):
    income_query = select(func.sum(Transaction.amount)).where(Transaction.type == 'income')
    expense_query = select(func.sum(Transaction.amount)).where(Transaction.type == 'expense')
    income_result = await db.execute(income_query)
    expense_result = await db.execute(expense_query)

    income = income_result.scalar() or 0.0
    expense = expense_result.scalar() or 0.0

    balance = income - expense

    return {
        "income": income,
        "expense": expense,
        "balance": balance
    }


async def get_report_by_datetime(db: AsyncSession):
    stmt = (
        select(
            func.date_trunc("minute", Transaction.date).label("datetime"),
            func.sum(
                case((Transaction.type == "income", Transaction.amount), else_=0)
            ).label("income"),
            func.sum(
                case((Transaction.type == "expense", Transaction.amount), else_=0)
            ).label("expense"),
        )
        .group_by("datetime")
        .order_by("datetime")
    )

    result = await db.execute(stmt)
    rows = result.all()

    return [
        ReportByDateTimeSchema(datetime=row.datetime, income=row.income, expense=row.expense)
        for row in rows
    ]