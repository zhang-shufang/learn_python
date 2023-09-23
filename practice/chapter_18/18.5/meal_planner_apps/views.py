from django.shortcuts import render

# Create your views here.
def index(request):
    """餐饮笔记主页"""
    return render(request, 'meal_planner_apps/index.html')
    