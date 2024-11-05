from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Modelserializer):
    class Meta:
        model = Task
        fields = '__all__'