from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView, name='blog-list'),
    path('edit/<int:pk>', views.BlogDetails, name='blog_details'),
]