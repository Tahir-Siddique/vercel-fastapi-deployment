from fastapi import FastAPI
from api.v1.endpoints import router as api_router
from os import getenv

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello, this is the LLM comparison api."}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(getenv("PORT", 8000)), reload=True)