from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField()
    cook = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name