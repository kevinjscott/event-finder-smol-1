```python
import sys
from scrapers.serpapi_search import search_events
from scrapers.golf_event_scraper import scrape_event
from utils.data_storage import store_data, reset_data_file
from utils.logger import log_message

def main(location):
    # Reset data and log files
    reset_data_file()
    log_message("Data file reset", "debug")

    # Search for golf events
    log_message(f"Searching for golf events in {location}", "status")
    event_pages = search_events(location)

    # Scrape each event page
    for page in event_pages:
        log_message(f"Scraping event page: {page}", "status")
        event_data = scrape_event(page)
        if event_data:
            store_data(event_data)
            log_message(f"Stored data for event: {event_data['event_name']}", "status")
        else:
            log_message(f"No data found for page: {page}", "debug")

    log_message("Scraping completed", "status")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <location>")
        sys.exit(1)

    location = sys.argv[1]
    main(location)
```