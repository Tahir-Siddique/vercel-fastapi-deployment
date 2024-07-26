import os
from dotenv import load_dotenv
import requests

load_dotenv()

VERCEL_BLOB_STORAGE_URL = os.getenv("VERCEL_BLOB_STORAGE_URL")

class StorageService:
    async def save_responses(self, data: dict):
        try:
            response = requests.post(VERCEL_BLOB_STORAGE_URL, json=data)
            return response.json()
        except:
            return data