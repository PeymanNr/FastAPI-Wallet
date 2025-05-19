from sqlalchemy import create_engine
from databases import Database
from db.models import Base

DATABASE_URL = "postgresql://ipeymani:932319361@localhost:5432/fastapiwallet"

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

def create_tables():
    Base.metadata.create_all(bind=engine)