from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name
    
class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=200)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
