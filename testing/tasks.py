from time import sleep

from celery import shared_task
from django.core.mail import send_mail

from celery.schedules import crontab


@shared_task
def func_sum(a, b):
    sleep(10)
    return a + b


@shared_task
def send_daily_test_report():
    emails = ['tima.akulich@gmail.com']
    send_mail(
        subject='Test task',
        message='test',
        from_email='admin@google.com',
        recipient_list=emails
    )


SCHEDULE = {
    # 'send_daily_test_report': {
    #     'task': 'testing.tasks.send_daily_test_report',
    #     'args': (),
    #     'options': {},
    #     'schedule': timedelta(seconds=5)
    # },
    'send_daily_test_report_1': {
        'task': 'testing.tasks.send_daily_test_report',
        'args': (),
        'options': {},
        'schedule': crontab(day_of_week=1, minute='*/1')
    }
}
