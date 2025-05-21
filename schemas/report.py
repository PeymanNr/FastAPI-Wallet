from pydantic import BaseModel
from datetime import datetime

class BalanceReportSchema(BaseModel):
    income: float
    expense: float
    balance: float

class ReportByDateTimeSchema(BaseModel):
    datetime: datetime
    income: float
    expense: float