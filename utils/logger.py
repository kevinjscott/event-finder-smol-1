```python
import logging

LOG_FILENAME = 'debug.log'

def setup_logger():
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, 
                        format='%(asctime)s %(levelname)s %(message)s', 
                        datefmt='%m/%d/%Y %I:%M:%S %p')

def log_message(message, level='info'):
    if level == 'debug':
        logging.debug(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    else:
        logging.info(message)

def reset_log_file():
    open(LOG_FILENAME, 'w').close()
```