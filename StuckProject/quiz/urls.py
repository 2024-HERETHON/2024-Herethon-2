from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),

    # 폴더
    path('folder/<int:folder_id>/', view_folder, name='folder-view'),
    path('folder/add/<int:parent_id>/', add_folder, name='add-folder'),
    path('folder/move/<int:folder_id>/to/<int:parent_id>/', move_folder, name='move-folder'),

    # 퀴즈
    path('folder/<int:folder_id>/create-quiz/', create_question, name = 'create-quiz'),
    path('folder/<int:folder_id>/testing/<int:quiz_id>/', test, name = "test"),
    path('folder/<int:folder_id>/result/<int:quiz_id>/', quiz_results, name="quiz-results"),
    path('folder/<int:folder_id>/view-all-questions/<int:quiz_id>/', view_questions, name = "view-questions"),
    path('folder/<int:folder_id>/view-wrong-questions/<int:quiz_id>/', view_wrong_questions, name="view-wrong-questions"),
    path('folder/<int:folder_id>/download-quiz-as-pdf/<int:quiz_id>/', save_quiz_as_pdf, name="save-quiz-as-pdf"),
    path('folder/<int:folder_id>/download-quiz-as-word/<int:quiz_id>/', save_quiz_as_word, name='save-quiz-as-word'),
]