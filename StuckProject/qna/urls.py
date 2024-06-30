from django.urls import path
from .views import *

app_name = 'qna'

urlpatterns = [
    path('select-folder/<int:folder_id>/', select_folder, name='select-folder'),
    path('folder/add/<int:parent_id>/', add_folder, name='add-folder'),
    path('folder/<int:folder_id>/create-question-room/', create_question_room, name="create-question-room"),
    path('folder/<int:folder_id>/enter-question-room/<int:question_room_id>/', enter_question_room, name="enter-question-room")
]