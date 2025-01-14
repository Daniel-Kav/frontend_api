from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tracker(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.FloatField()  # in cm
    weight = models.FloatField()  # in kg
    fitness_goal = models.CharField(max_length=255)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise = models.CharField(max_length=255)
    duration = models.DurationField()  # in minutes
    calories_burned = models.FloatField()

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal_name = models.CharField(max_length=255)
    calories = models.FloatField()

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    target_weight = models.FloatField()
    
