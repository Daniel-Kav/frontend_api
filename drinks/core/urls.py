from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('drinks/', views.drink_list, name='drink_list'),
    path('drinks/<int:pk>', views.drink_detail, name='drink_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)