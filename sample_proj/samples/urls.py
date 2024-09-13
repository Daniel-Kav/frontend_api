from . import views
from  django.urls import path


urlpatterns = [
    path('', views.home_view, name='home'),
    path('new/', views.new_sample_view, name='new_sample'),
    path('edit/<int:pk>', views.edit_sample, name='edit_sample'),

]