from pydantic import BaseModel

class BalanceReportSchema(BaseModel):
    income: float
    expense: float
    balance: float