from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length= 200)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes')
    question = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    progress = models.DecimalField(max_digits=5, decimal_places=2, default= 0)

    def __str__(self):
        return f"{self.student.username} is enrolled in {self.course.title}."

