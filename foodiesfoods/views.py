from django.shortcuts import render, redirect

from .models import Food, FoodRequest
from .forms import RatingForm


def index(request):
    """The home page"""
    return render(request, 'foodiesfoods/index.html')


def foods(request):
    """The home page"""
    foods = Food.objects.order_by('date_added')
    context = {'foods': foods}
    return render(request, 'foodiesfoods/foods.html', context)


def food(request, food_id):
    food = Food.objects.get(id=food_id)
    ratings = food.foodrequest_set.order_by('-date_added')
    context = {'food': food, 'ratings': ratings}
    return render(request, 'foodiesfoods/food.html', context)


def rating(request, food_id):
    food = Food.objects.get(id=food_id)

    if request.method != 'POST':
        form = RatingForm()
    else:
        form = RatingForm(data=request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.food = food
            rating.save()
            return redirect('foodiesfoods:food', food_id=food_id)

    context = {'food': food, 'form': form}
    return render(request, 'foodiesfoods/rating.html', context)
