from django.contrib import admin
from .models import Course,Lesson,Quiz,Enrollment

# Register your models here.
admin.site.register(Course,Lesson,Quiz,Enrollment)
