from django.urls import path
from . import views

urlpatterns = [
    path('',views.getBlogs, name='home'),
    path('new-blog/',views.addBlog, name='addBlog'),
    path('edit-blog/<int:pk>/',views.editBlog,name='editblog')

]