import os
import requests
from typing import Dict, List


class LLMService:
    def __init__(self):
        self.llm_apis = {
            "openai": {
                "url": "https://api.openai.com/v1/chat/completions",
                "headers": {"Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"},
                "json": {"model": "gpt-4o-mini", "max_tokens": 150},
            },
            "anthropic": {
                "url": "https://api.anthropic.com/v1/messages",
                "headers": {
                    "X-API-Key": os.environ.get('ANTHROPIC_API_KEY'),
                    "Content-Type": "application/json",
                    "anthropic-version": "2023-06-01",
                },
                "json": {"model": "claude-3-haiku-20240307", "max_tokens": 150},
            },
        }

    def prepare_openai_json(self, api_config, prompt):
        return {
                **api_config["json"],
                "messages": [{"role": "user", "content": prompt}]
            }


    def prepare_anthropic_json(self, api_config, prompt):
        return {
                **api_config["json"],
                "messages": [{"role": "user", "content": prompt}]
            }


    def call_llm_api(self, name: str, prompt: str) -> Dict:
        api_config = self.llm_apis[name]
        prepare_json = getattr(self, f"prepare_{name}_json")
        json_data = prepare_json(api_config, prompt)
        response = requests.post(api_config["url"], headers=api_config["headers"], json=json_data)
        return {"name": name, "response": response.json()}

    async def compare_llms(self, prompt: str) -> List[Dict]:
        return [self.call_llm_api(name, prompt) for name in self.llm_apis.keys()]