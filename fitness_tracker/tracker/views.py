from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html')

from rest_framework import viewsets
from .models import UserProfile, Workout, Meal, Goal
from .serializers import UserProfileSerializer, WorkoutSerializer, MealSerializer, GoalSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

