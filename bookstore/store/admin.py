from django.contrib import admin
from rest_framework import serializers
from .models import Publisher,Author,Book

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)