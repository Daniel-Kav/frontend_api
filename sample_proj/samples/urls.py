from . import views
from  django.urls import path


urlpatterns = [
    path('', views.home_view, name='home'),
    path('new/', views.new_sample_view, name='new_sample'),
]