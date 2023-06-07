import requests
import os

api_endpoint = "https://api.openai.com/v1/completions"
api_key = ""

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

arg = input('Lança a braba!')

request_data = {
    "model": "text-davinci-003",
    "prompt": f"{arg}",
    "max_tokens": 500,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    print(response.json()["choices"][0]["text"])
else:
    print(f"Request failed with status code: {str(response.status_code)}")
