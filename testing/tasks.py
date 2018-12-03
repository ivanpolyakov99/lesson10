from time import sleep

from celery import shared_task


@shared_task
def func_sum(a, b):
    sleep(10)
    return a + b
