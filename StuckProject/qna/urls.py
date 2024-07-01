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
    path('delete/<int:question_room_id>/', delete_question_room, name='delete-question-room'),
    path('move/<int:current_folder_id>/<int:question_room_id>/to/<int:move_folder_id>/', move_question_room, name='move-question-room'),

    # 스크랩
    path('folder/<int:folder_id>/scrap-question-room/<int:question_room_id>/', add_scrap_question_room, name='add-scrap-question-room'),
    path('folder/<int:folder_id>/remove-scrap-question-room/<int:question_room_id>/', remove_scrap_question_room, name='cancel-scrap-question-room'),

    # 저장
    path('folder/<int:folder_id>/save-chat-as-pdf/<int:question_room_id>/', save_chat_as_pdf, name='save-chat-as-pdf'),
    path('folder/<int:folder_id>/save-chat-as-word/<int:question_room_id>/', save_chat_as_word, name='save-chat-as-word'),

]