from django.urls import path
from .views import *

app_name = 'qna'

urlpatterns = [
    path('select-folder/<int:folder_id>/', select_folder, name='select-folder'),
    path('folder/add/<int:parent_id>/', add_folder, name='add-folder'),
    path('folder/<int:folder_id>/create-question-room/', create_question_room, name="create-question-room"),
    path('folder/<int:folder_id>/enter-question-room/<int:question_room_id>/', enter_question_room, name="enter-question-room"),
    path('folder/<int:folder_id>/save-question-memo/<int:question_room_id>/', save_question_memo, name="save-question-memo"),
    path('folder/<int:folder_id>/save-memo-as-pdf/<int:question_room_id>/', save_memo_as_pdf, name="save-memo-as-pdf"),
    path('folder/<int:folder_id>/save-memo-as-word/<int:question_room_id>/', save_memo_as_word, name="save-memo-as-word"),
    
]