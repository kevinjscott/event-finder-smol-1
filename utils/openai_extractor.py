```python
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_data(text, url):
    try:
        response = openai.Answer.create(
            search_model="davinci",
            documents=[text],
            question=f"Extract details about the golf event at {url}",
            stop=["\n"],
            log_level="info",
            logprobs=10,
            lls_model="text-davinci-002",
            max_responses=1,
            stop_sequences=["\n"],
            temperature=0.5,
        )

        data = response['choices'][0]['text'].strip()
        return data
    except Exception as e:
        print(f"Error in extracting data from OpenAI: {e}")
        return None
```