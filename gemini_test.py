
import os
import time
import json
from dotenv import load_dotenv
from openai import OpenAI, APIStatusError

load_dotenv()

api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL")
model = os.getenv("LLM_MODEL")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": "What is machine learning?"
        }
    ]
}

try:
    start = time.perf_counter()

    response = client.chat.completions.create(**payload)

    elapsed = time.perf_counter() - start

    result = {
        "status": "success",
        "http_method": "POST",
        "http_status": 200,
        "model": model,
        "question": payload["messages"][0]["content"],
        "answer": response.choices[0].message.content,
        "response_time_seconds": round(elapsed, 2)
    }

except APIStatusError as e:
    result = {
        "status": "error",
        "http_method": "POST",
        "http_status": e.status_code,
        "model": model,
        "error": e.message,
        "response_time_seconds": round(
            time.perf_counter() - start, 2
        )
    }

except Exception as e:
    result = {
        "status": "error",
        "http_method": "POST",
        "error": str(e),
        "response_time_seconds": round(
            time.perf_counter() - start, 2
        )
    }

# Print valid JSON
print(json.dumps(result, indent=4, ensure_ascii=False))
