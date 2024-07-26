import pytest
from dotenv import load_dotenv
from app.services.llm_service import LLMService
from app.services.storage_service import StorageService

def pytest_configure(config):
    load_dotenv('.env.test') 


@pytest.fixture
def storage_service():
    return StorageService()


@pytest.fixture
def llm_service():
    return LLMService()