from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Transaction



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
