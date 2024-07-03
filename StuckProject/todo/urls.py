from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('todo_list/', views.todo_list, name='todo_list'),
    path('todo/complete/<int:pk>/', views.complete_todo, name='complete_todo'),
]
