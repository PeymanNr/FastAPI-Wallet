from db.models import Transaction
from schemas.transaction import TransactionCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_transaction(db: AsyncSession, transaction: TransactionCreate):
    new_transaction = Transaction(
        amount=transaction.amount,
        type=transaction.type,
        description=transaction.description,
    )
    db.add(new_transaction)
    await db.commit()
    await db.refresh(new_transaction)
    return new_transaction