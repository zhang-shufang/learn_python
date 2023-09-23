"""定义 meal_planner_apps 的 URL 模式"""

from django.urls import path

from . import views

app_name = 'meal_planner_apps'
urlpatterns = [
    # Main page
    path('', views.index, name='index'),
]