from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.blog_index, name='index'),
    path('articles/<str:id>/', views.articles, name='articles'),
    
]