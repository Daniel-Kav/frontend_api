from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name= 'home'),
    path('new/', views.create_post,name= "new-post" ),
    path('new/<int:pk>/', views.post_detail, name = "post_detail"),
    path('edit/<int:pk>', views.edit_post, name='edit_post'),
    path('del/<int:pk>/', views.del_post, name='delete_post')
]