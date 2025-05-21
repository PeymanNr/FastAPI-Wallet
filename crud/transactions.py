from db.models import Transaction
from schemas.transaction import TransactionCreateSchema
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy import select


async def create_transaction(db: AsyncSession, transaction: TransactionCreateSchema):
    new_transaction = Transaction(
        amount=transaction.amount,
        type=transaction.type,
        description=transaction.description,
    )
    db.add(new_transaction)
    await db.commit()
    await db.refresh(new_transaction)
    return new_transaction

async def get_transactions(
    db: AsyncSession,
    type: Optional[str] = None,
    sort: str = "desc"
) -> List[Transaction]:
    stmt = select(Transaction)

    if type:
        stmt = stmt.where(Transaction.type == type)

    if sort == "asc":
        stmt = stmt.order_by(Transaction.date.asc())
    else:
        stmt = stmt.order_by(Transaction.date.desc())

    result = await db.execute(stmt)
    return result.scalars().all()