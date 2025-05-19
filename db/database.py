from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from databases import Database
from contextlib import asynccontextmanager
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = "postgresql+asyncpg://ipeymani:932319361@localhost:5432/fastapiwallet"

database = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session


