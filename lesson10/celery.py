import os
import django

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson10.settings')
django.setup()


from testing.tasks import SCHEDULE as TESTING_SCHEDULE
app = Celery('lesson10')


SCHEDULE = {}
SCHEDULE.update(TESTING_SCHEDULE)
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = SCHEDULE
app.autodiscover_tasks()
