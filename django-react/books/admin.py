from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book
        fields = '__all__'

admin.site.register(Book, BookAdmin)
