from django.urls import path
from . import views

urlpatterns = [
    path('publishers',views.PublisherCreateView.as_view(), name='publisher-list-create'),
    path('publishers/<int:pk>',views.PUblisherDetailView.as_view(), name='publisher-detail'),

    path('authors',views.AuthorCreateView.as_view(),name='author-list-create'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-details'),

    path('books',views.BookCreateView.as_view(),name='book-list-create'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]