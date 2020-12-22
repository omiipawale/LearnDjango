from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.taskSubmit, name='submit'),
    path('delete', views.taskDelete, name='delete'),
]
