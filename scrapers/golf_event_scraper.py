```python
import scrapy
from utils.openai_extractor import extract_data
from utils.logger import log_message

class GolfEventScraper(scrapy.Spider):
    name = "golf_event_scraper"

    def __init__(self, event_urls, *args, **kwargs):
        super(GolfEventScraper, self).__init__(*args, **kwargs)
        self.start_urls = event_urls

    def parse(self, response):
        log_message("Scraping event page: " + response.url, "debug")
        page_text = response.text
        event_data = extract_data(page_text, response.url)
        yield event_data
```
This is the code for the `scrapers/golf_event_scraper.py` file. It defines a Scrapy spider that takes a list of event URLs as input, scrapes each page, and yields the extracted data. The `extract_data` function from `utils/openai_extractor.py` is used to extract specific data from the page text and URL. Debug messages are logged using the `log_message` function from `utils/logger.py`.