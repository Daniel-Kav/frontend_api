from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    read = models.BooleanField()

    def __str__(self):
        return self.title
