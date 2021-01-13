"""Defines url patterns for foodiesfoods."""

from django.urls import path
from . import views

app_name = 'foodiesfoods'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('foods/', views.foods, name='foods'),
    path('foods/<int:food_id>/', views.food, name='food'),
    path('rating/<int:food_id>/', views.rating, name='rating'),
]
