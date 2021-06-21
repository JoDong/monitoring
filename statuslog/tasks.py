import django

from config.celery import app
from statuslog.views import status

django.setup()


@app.task
def debug_task():
    print('Run Celery debug_task()')


@app.task
def proc_status():
    print('Run Celery proc_status()')
    status()

