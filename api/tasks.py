from celery import shared_task
from time import sleep
from PIL import Image
@shared_task(name="first_task")
def add(x, y):
    sleep(20)
    print("sum = ",x+y)

@shared_task(name="thumbnail_creater")
def thumbnail_task(image):
    sleep(10)
    pil_image = Image.open(image)
    pil_image.resize((100, 100))
    pil_image.save('temp.jpg')