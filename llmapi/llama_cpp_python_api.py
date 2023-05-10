"""
first implementation of a api call to llama-cpp-python
"""
import os
import re
import json
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Load environment variables from .env file
load_dotenv(dotenv_path)

# URL of the API endpoint
api_url = os.getenv("LLAMA_CCP_API_URL")
llama_temperature = os.getenv("LLAMA_TEMPERATURE")
llama_tokens = os.getenv("LLAMA_MAX_TOKEN")
llama_echo = os.getenv("LLAMA_ECHO")
llama_request_timeout = int(os.getenv("LLAMA_REQUEST_TIMEOUT"))

# Read the prompt text from a file
with open("prompt_testing_ip_moved.txt", "r") as f:
    prompt = f.read().strip()

# Request body
data = {
    "temperature": llama_temperature,
    "max_tokens": llama_tokens,
    "stop": ["###"],
    "prompt": prompt
}

# Send the POST request to the API
try:
    response = requests.post(api_url, json=data, timeout=llama_request_timeout)
except requests.exceptions.RequestException as e:
    print(f"An error occurred while sending the request: {e}")
    exit(1)

# Check if the request was successful
if response.status_code == requests.codes.ok:
    # Strip the string of characters
    response_content_string = response.content.decode('utf-8').replace("\\n", "").replace("\\", "")
    print (response_content_string)
    with open('response.txt', 'w') as f:
        f.write(response_content_string)

    match = re.search(r'{"thoughts".*?"}}}', response_content_string)
    if match:
        # extract JSON object using slicing
        json_str = match.group()
        print(json_str)
    else:
        print("No JSON object found")
else:
    print(f"HTTP error occurred: {response.status_code}")
