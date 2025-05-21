from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TransactionCreateSchema(BaseModel):
    amount: float = Field(..., gt=0, description="Transaction amount, must be positive")
    type: str = Field(..., min_length=3, max_length=50, description="Transaction type")
    description: Optional[str] = Field(None, min_length=3, max_length=255, description="Short description of the transaction")

class TransactionOutSchema(BaseModel):
    id: int
    amount: float
    description: Optional[str]
    date: datetime

    class Config:
        orm_mode = True