"""define the url model of blog_apps"""
from django.urls import path

from . import views

app_name = 'blog_apps'
urlpatterns = [
    # main page
    path('', views.blogs, name='blogs'),
    # blog page
    path('blogs/<int:blog_id>/', views.blog, name='blog'),
    # add new blog page
    path('new_blog/', views.new_blog, name='new_blog'),
    # add new article page
    path('new_article/<int:blog_id>/', views.new_article, name='new_article'),
    # edit article page
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
]