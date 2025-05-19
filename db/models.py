from datetime import datetime
from sqlalchemy import Column, Integer, String , Float, DateTime
from db.database import Base

class Transaction(Base):
    __tablename__="transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)