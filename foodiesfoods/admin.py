from django.contrib import admin

from .models import Food, FoodRequest

admin.site.register(Food)
admin.site.register(FoodRequest)
