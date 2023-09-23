"""定义 pizzaria_apps 的 URL 模式"""
from django.urls import path

from . import views

app_name = 'pizzaria_apps'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]