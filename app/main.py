from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from api.v1.endpoints import router as api_router
from os import getenv

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello, this is the LLM comparison api."}
