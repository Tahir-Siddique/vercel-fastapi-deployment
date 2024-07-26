from time import time
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from app.api.v1.endpoints import router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router, prefix="/api/v1")

@app.get('/')
async def hello():
    return {'description': "This FastAPI-based microservice allows users to compare responses from OpenAI's ChatGPT and Anthropic's LLM by submitting a single prompt. The API leverages asynchronous requests for efficient response retrieval and secures access with API key authentication. It stores prompts and responses in Vercel Blob Storage and is designed for seamless deployment as a serverless function on Vercel. The project includes a comprehensive test suite to ensure reliability and maintainability."}