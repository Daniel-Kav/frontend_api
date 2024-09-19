# from django.shortcuts import render, get_object_or_404
from .forms import CoursesForm, LessonForm, QuizForm
from .models import Course,Lesson,Quiz, Enrollment

# # Create your views here.
# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'lms/course_list.html', {'courses': courses})

# #couse details and lessons
# def course_details(request, pk):
#     course = get_object_or_404(Course, pk=pk)
#     lessons = course.lessons.all()
#     return render(request, 'lms/course_details.html',{'course':course, 'lessons':lessons})



from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CoursesForm, LessonForm

class LandingPageView(TemplateView):
    template_name = 'lms/landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_courses'] = Course.objects.all()[:3]  # Get 3 featured courses
        return context

class CourseListView(ListView):
    model = Course
    template_name = 'lms/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'lms/course_details.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.object.lessons.all()
        return context

class CustomLoginView(LoginView):
    template_name = 'lms/login.html'
    success_url = reverse_lazy('course_list')

class RegistrationView(CreateView):
    template_name = 'lms/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class AddCourseView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    form_class = CoursesForm
    template_name = 'lms/add_course.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

class AddLessonView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'lms/add_lesson.html'

    def form_valid(self, form):
        course = Course.objects.get(pk=self.kwargs['course_id'])
        form.instance.course = course
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('course_detail', kwargs={'pk': self.kwargs['course_id']})

    def test_func(self):
        course = Course.objects.get(pk=self.kwargs['course_id'])
        return self.request.user == course.teacher
