```python
import serpapi
from utils.logger import log_message
from config import SERPAPI_API_KEY

def search_events(location):
    client = serpapi.GoogleSearchResults({"q": f"golf tournaments in {location}", "api_key": SERPAPI_API_KEY})
    results = []
    page = 1

    while True:
        log_message(f"Fetching page {page} for {location}")
        data = client.get_json()
        events = data.get('events_results', [])

        for event in events:
            if event_in_future(event):
                results.append(event)

        if 'next' not in data:
            break

        client.params_dict["start"] = data['next']
        page += 1

    return results

def event_in_future(event):
    # Logic to check if the event is in the future
    # This is a placeholder and should be replaced with actual logic
    return True
```