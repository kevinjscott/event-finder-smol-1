```python
# config.py

# API Keys
SERPAPI_API_KEY = "your-serpapi-api-key"
OPENAI_API_KEY = "your-openai-api-key"

# File Paths
RESULTS_FILE = "results.json"
LOG_FILE = "debug.log"

# Search Query Template
SEARCH_QUERY_TEMPLATE = "golf tournaments in {}"

# Pagination Settings
SERPAPI_PAGINATION_LIMIT = 10

# Event Data Schema
EVENT_DATA_SCHEMA = {
    "today_date": None,
    "event_date": None,
    "is_future_event": None,
    "location": None,
    "city": None,
    "state": None,
    "registration_link": None,
    "tickets_link": None,
    "event_summary": None,
    "registration_status": None,
    "is_military_related": None,
    "is_charitable_event": None,
    "charity_description": None,
    "host_organization": None,
    "host_description": None,
    "is_spammy": None,
    "is_canonical_source": None,
    "is_playable_event": None
}
```