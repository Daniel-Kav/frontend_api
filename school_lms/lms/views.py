from django.shortcuts import render, get_object_or_404
from .forms import CoursesForm, LessonForm, QuizForm
from .models import Course,Lesson,Quiz, Enrollment

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'lms/course_list.html', {'courses': courses})

#couse details and lessons
def course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lessons = course.lessons.all()
    return render(request, 'lms/course_details.html',{'course':course, 'lessons':lessons})
