from celery import shared_task
from time import sleep

@shared_task(name="first_task")
def add(x, y):
    sleep(20)
    print("sum = ",x+y)