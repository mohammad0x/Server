import requests
import schedule
import time
from datetime import datetime


def send_request1():
    url = 'http://127.0.0.1:8000/admin'

    response = requests.get(url)

    if response.status_code == 200:
        print('ok1')
    else:
        print('no1', response.status_code)


def send_request2():
    url = 'http://127.0.0.1:8000/'

    response = requests.get(url)

    if response.status_code == 200:
        print('ok2')
    else:
        print('no2', response.status_code)


def schedule_request():
    schedule.every().day.at("20:00").do(send_request1)
    schedule.every().day.at("21:00").do(send_request2)


schedule_request()

while True:
    schedule.run_pending()
    time.sleep(1)
