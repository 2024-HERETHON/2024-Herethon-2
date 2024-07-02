from django.urls import path
from .views import *


app_name = 'quiz'

urlpatterns = [
    path('', home, name="home"),

    # 폴더
    path('folder/<int:folder_id>/', view_folder, name='folder-view'),
    path('folder/add/<int:parent_id>/', add_folder, name='add-folder'),
    path('folder/move/<int:folder_id>/to/<int:parent_id>/', move_folder, name='move-folder'),
    path('quiz/move/<int:current_folder_id>/<int:quiz_id>/to/<int:move_folder_id>/', move_quiz, name='move-quiz'),
    path('select-folder/<int:folder_id>/', select_folder, name='select-folder'),
    path('search-folder/<int:folder_id>/', search_folder, name="search-folder"),

    # 퀴즈
    path('folder/<int:folder_id>/create-quiz/', create_question, name = 'create-quiz'),
    path('folder/<int:folder_id>/testing/<int:quiz_id>/', test, name = "test"),
    path('folder/<int:folder_id>/result/<int:quiz_id>/', quiz_results, name="quiz-results"),
    path('folder/<int:folder_id>/view-all-questions/<int:quiz_id>/', view_questions, name = "view-questions"),
    path('folder/<int:folder_id>/view-wrong-questions/<int:quiz_id>/', view_wrong_questions, name="view-wrong-questions"),
    path('folder/<int:folder_id>/download-quiz-as-pdf/<int:quiz_id>/', save_quiz_as_pdf, name="save-quiz-as-pdf"),
    path('folder/<int:folder_id>/download-quiz-as-word/<int:quiz_id>/', save_quiz_as_word, name='save-quiz-as-word'),

    # 스크랩
    path('folder/<int:folder_id>/scrap/', add_scrap_folder, name='add-scrap-folder'),
    path('folder/<int:folder_id>/cancel-scrap/', remove_scrap_folder, name='cancel-scrap-folder'),
    path('folder/<int:folder_id>/scrap-quiz/<int:quiz_id>/', add_scrap_quiz, name='add-scrap-quiz'),
    path('folder/<int:folder_id>/cancel-scrap-quiz/<int:quiz_id>/', remove_scrap_quiz, name='cancel-scrap-quiz'),

    # 삭제
    path('folder/delete/<int:folder_id>/', delete_folder, name='delete-folder'),
    path('quiz/delete/<int:quiz_id>/', delete_quiz, name='delete-quiz'),

    # 최근 열어본 퀴즈
    
    
    path('home/', get_rate, name='get_rate'),
]