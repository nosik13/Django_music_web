"""Здесь происходит огловление url страниц для see_app
пример построения строки: path('название страницы/', views.модель, name='имя модели'),"""

from django.urls import path
from . import views

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('timetable/', views.timetable, name='timetable')
]
