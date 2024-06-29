from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('category/<int:folder_id>/', view_folder, name='folder-view'),
    path('category/add/<int:parent_id>/', add_folder, name='add-folder'),
]