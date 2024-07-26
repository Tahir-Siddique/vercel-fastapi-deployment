from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import JSONResponse
from app.shemas.prompt import LLMResponse, PromptRequest
from app.utils.auth import get_api_key
from app.services.llm_service import LLMService
from app.services.storage_service import StorageService
import logging

router = APIRouter()

llm_service = LLMService()
storage_service = StorageService()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/compare-llms", response_model=LLMResponse)
async def get_llm_responses(prompt_request: PromptRequest, background_tasks: BackgroundTasks, api_key: str = Depends(get_api_key)):
    try:
        prompt_responses = await llm_service.compare_llms(prompt_request.prompt)
        return JSONResponse(await storage_service.save_responses({"prompt": prompt_request.prompt, "responses": prompt_responses}))
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return JSONResponse({"status": "crashed", "detail":str(e)})