from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.chatPage, name="chat-page"),

    #login
    path('auth/login', LoginView.as_view(template_name= 'chat/LoginPage.html'), name= 'login-user   '),
    path('auth/logout/', LogoutView.as_view(), name='logout-user'),
]