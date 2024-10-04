from django.db import models

# Create your models here

class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateField(auto_now_add= True)
    