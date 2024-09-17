# game/urls.py
from django.urls import path
from .views import tic_tac_toe

urlpatterns = [
    path('', tic_tac_toe, name='tic_tac_toe'),
]
