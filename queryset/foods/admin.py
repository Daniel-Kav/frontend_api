from django.contrib import admin
from .models import Food


# class FoodAdmin(admin.Model):...
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', ]

admin.site.register(Food, FoodAdmin)