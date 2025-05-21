from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from databases import Database
from sqlalchemy.orm import DeclarativeBase
from config import settings


DATABASE_URL = settings.DATABASE_URL

database = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with async_session() as session:
        yield session


