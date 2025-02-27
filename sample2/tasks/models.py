from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __init__(self):
        return self.name

