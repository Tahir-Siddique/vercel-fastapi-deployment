import json
import uuid
from dotenv import load_dotenv
import vercel_blob

load_dotenv()

class StorageService:
    async def save_responses(self, data: dict):
        try:
            data["blob_url"] = vercel_blob.put(str(uuid.uuid4(), json.dumps(data).encode('utf-8')))
        except Exception as e:
            data["blob_url"] = str(e)
        return data