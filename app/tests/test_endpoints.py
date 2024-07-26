import pytest
from fastapi.testclient import TestClient
from app.services.llm_service import LLMService
from app.services.storage_service import StorageService
from app.api.v1.endpoints import router as api_router
from app.main import app

client = TestClient(app)

@pytest.fixture
def mock_llm_service(mocker):
    mock = mocker.patch('app.services.llm_service.LLMService.call_llm_api')
    mock.return_value = [
        {"name": "chatgpt", "response": "ChatGPT response"},
        {"name": "anthropic", "response": "Anthropic response"}
    ]
    return mock

@pytest.fixture
def mock_storage_service(mocker):
    mock = mocker.patch('app.services.storage_service.StorageService.save_responses')
    mock.return_value = {
        "url": "https://example.com/blob/12345",
        "prompt": "Test prompt",
        "responses": [
            {"name": "chatgpt", "response": "ChatGPT response"},
            {"name": "anthropic", "response": "Anthropic response"}
        ]
    }
    return mock

def test_get_llm_responses(mock_llm_service, mock_storage_service):
    response = client.post(
        "/api/v1/compare-llms",
        json={"prompt": "Test prompt"},
        headers={"api_key": "your_api_key"}
    )
    assert response.status_code == 200
    assert "responses" in response.json()

def test_get_llm_responses_invalid_api_key():
    response = client.post(
        "/api/v1/compare-llms",
        json={"prompt": "Test prompt"},
        headers={"api_key": "invalid-api-key"}
    )
    assert response.status_code == 403
