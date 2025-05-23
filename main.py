from fastapi import FastAPI
from db.database import database
from routers.transactions import router as transactions_router
from routers.reports import router as reports_router

app = FastAPI(title="Simple Finance Service")
app.include_router(transactions_router)
app.include_router(reports_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()