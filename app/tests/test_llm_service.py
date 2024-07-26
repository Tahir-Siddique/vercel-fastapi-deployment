import pytest
from unittest.mock import patch

@pytest.mark.asyncio
async def test_compare_llms(llm_service, mocker):
    mock_call_llm_api = mocker.patch.object(llm_service, 'call_llm_api')
    mock_call_llm_api.side_effect = [
        {"name": "openai", "response": "OpenAI response"},
        {"name": "anthropic", "response": "Anthropic response"}
    ]

    result = await llm_service.compare_llms("Test prompt")

    assert len(result) == 2
    assert result[0]["name"] == "openai"
    assert result[1]["name"] == "anthropic"

def test_call_llm_api(llm_service, mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"choices": [{"message": {"content": "API response"}}]}

    with patch('requests.post', return_value=mock_response):
        result = llm_service.call_llm_api("openai", "Test prompt")

    assert result["name"] == "openai"
    assert "response" in result
    assert result["response"] == {"choices": [{"message": {"content": "API response"}}]}