from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title

class Tag(models.Model):
    value = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.value
