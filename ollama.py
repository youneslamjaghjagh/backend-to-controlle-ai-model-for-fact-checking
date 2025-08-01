import requests
class OllamaAPI:
    def __init__(self, api_url="http://localhost:11434/api/generate", model_name="llama3.2:3b") :
        self.api_url = api_url
        self.model_name = model_name

    def generate_response(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error communicating with Ollama API: {str(e)}")



