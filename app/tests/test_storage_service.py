import pytest
from unittest.mock import patch

@pytest.mark.asyncio
async def test_save_responses_success(storage_service, mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        "prompt": "Hello World",
        "responses": [],
        "blob_url": "https://example.com/blob/12345"
    }

    with patch('requests.post', return_value=mock_response):
        result = await storage_service.save_responses({"prompt": "Test", "responses": []})

    assert "blob_url" in result
    assert result["blob_url"] == "https://example.com/blob/12345"

@pytest.mark.asyncio
async def test_save_responses_failure(storage_service, mocker):
    with patch('requests.post', side_effect=Exception("Test error")):
        result = await storage_service.save_responses({"prompt": "Test", "responses": []})

    assert result == {"prompt": "Test", "responses": []}