from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView, name='blog-list'),
    path('details/<int:pk>', views.BlogDetails, name='blog_details'),
    path('delete/<int:pk>', views.BlogDelete, name='blog_delete'),
]