# tasks/urls.py
from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.task_main, name='task_main'),
    path('all/', views.task_list, name='task_list'),
    path('completed/', views.task_completed, name='task_completed'),
    path('<int:task_id>/', views.task_detail_all, name='task_detail_all'),
    path('completed/<int:task_id>/', views.task_detail, name='task_detail'),
]