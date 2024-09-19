from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('add-course/', views.AddCourseView.as_view(), name='add_course'),
    path('courses/<int:course_id>/add-lesson/', views.AddLessonView.as_view(), name='add_lesson'),
]


