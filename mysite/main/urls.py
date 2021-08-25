from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<slug:slug>/', views.user, name='user'),
    path('content/<str:pk>/', views.viewing_content, name='content')
]
