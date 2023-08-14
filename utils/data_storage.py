```python
import json
import os

RESULTS_FILE = "results.json"

def reset_results_file():
    if os.path.exists(RESULTS_FILE):
        os.remove(RESULTS_FILE)

def store_data(data):
    reset_results_file()
    with open(RESULTS_FILE, 'w') as f:
        json.dump(data, f, indent=4)
```