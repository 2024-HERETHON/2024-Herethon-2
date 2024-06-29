from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('category/<int:folder_id>/', view_folder, name='folder-view'),
    path('category/add/<int:parent_id>/', add_folder, name='add-folder'),
    path('folder/move/<int:folder_id>/to/<int:parent_id>/', move_folder, name='move_category'),
]