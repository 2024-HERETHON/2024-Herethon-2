from django.urls import path, register_converter
from accounts.converters import NegativeIntConverter
register_converter(NegativeIntConverter, 'negint')

from . import views

app_name = 'todo'

urlpatterns = [
    path('todo_list/<int:year>/<int:month>/<int:day>/<negint:offset>/', views.todo_list, name='todo_list'),
    path('todo/complete/<int:year>/<int:month>/<int:day>/<negint:offset>/<int:pk>/', views.complete_todo, name='complete_todo'),
    path('delete-routine/<int:year>/<int:month>/<int:day>/<negint:offset>/<int:pk>/', views.delete_routine, name='delete-routine'),

]
