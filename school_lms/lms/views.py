from django.shortcuts import render
from .forms import CoursesForm, LessonForm, QuizForm
from .models import Course,Lesson,Quiz, Enrollment

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'lms/course_list.html', {'courses': courses})