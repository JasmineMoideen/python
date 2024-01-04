from django.db import models

# Create your models here.
class Todo(models.Model):
    taskname=models.TextField()
    taskpriority=models.TextField()
    taskdate=models.DateField()