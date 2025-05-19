from fastapi import FastAPI
from db.database import database, create_tables

app = FastAPI(title="Simple Finance Service")

@app.on_event("startup")
async def startup():
    await database.connect()
    create_tables()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()