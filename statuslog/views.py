import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()



from statuslog.models import StatusLog


def status():
    response = requests.get('http://www.naver.com')
    print(response)
    log = response.elapsed.total_seconds()
    ping = int(round(log * 1000))
    code = response.status_code
    time_all = response.headers['Date']
    time_at = time_all[12:-4]
    print(f'시간:{time_at}, 처리시간:{ping}ms, 상태 코드: {code}')


sched = BackgroundScheduler()
sched.start()
sched.add_job(status, 'interval', seconds=5)

while True:
    print("Running main process...............")
    time.sleep(1)
