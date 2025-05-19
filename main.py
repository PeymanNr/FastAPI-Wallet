from fastapi import FastAPI

app = FastAPI(title="Simple Finance Service")
@app.get("/")
async def root():
    return {"message": "Hello World"}