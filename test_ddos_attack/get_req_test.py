import logging
import requests
import threading
import concurrent.futures
from datetime import datetime, timedelta


def thread_function():
    resp = requests.get('https://www.ukr.net/')
    logging.info("Thread finishing, %s, %s", resp, threading.current_thread().ident)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
        start_time = datetime.now()
        while True:
            if datetime.now() - start_time > timedelta(seconds=1):
                break
            executor.submit(thread_function)
