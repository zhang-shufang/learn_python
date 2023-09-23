"""定义 pizzaria_apps 的 URL 模式"""
from django.urls import path

from . import views

app_name = 'pizzaria_apps'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有披萨的页面
    path('pizzas/', views.pizzas, name='pizzas'),
    # 显示选定披萨及其馅料的页面
    path('pizzas/<int:pizza_id>', views.pizza, name='pizza'),
]