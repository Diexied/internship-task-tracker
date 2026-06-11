from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-task/', views.add_task, name='add_task'),
    path('view-tasks/', views.view_tasks, name='view_tasks'),
    path('about/', views.about, name='about'),
]