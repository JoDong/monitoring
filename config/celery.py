import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

CELERY_ALWAYS_EAGER = True
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul'
CELERY_ENABLE_UTC = False

BROKER_URL = CELERY_BROKER_URL
RESULT_BACKEND = CELERY_RESULT_BACKEND

app = Celery('core', backend=RESULT_BACKEND, broker=BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    CELERY_TIMEZONE='Asia/Seoul',
    CELERY_ENABLE_UTC=False,
    CELERY_BEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler',
)

app.autodiscover_tasks()
if __name__ == '__main__':
    app.start()
