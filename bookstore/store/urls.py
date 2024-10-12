from django.urls import path
from . import views

urlpatterns = [
    path('publishers',views.PublisherCreateView.as_view(), name='publisher-list-create'),
    path('publishers/<int:pk>',views.PUblisherDetailView.as_view(), name='publisher-detail')
]