import test
import requests
import time
import schedule



while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds