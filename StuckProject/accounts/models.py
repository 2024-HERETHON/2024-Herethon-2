from django.db import models
from django.contrib.auth.models import User
from quiz.models import Folder, Quiz


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    univ = models.TextField(max_length=100)
    semester = models.IntegerField()
    scrap_folders = models.ManyToManyField(Folder, through='ScrapFolder', related_name='folder_scrapped_by')
    scrap_quizs = models.ManyToManyField(Quiz, through="ScrapQuiz", related_name="quiz_scrapped_by")


# 폴더 스크랩 
class ScrapFolder(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'folder')


# 퀴즈 스크랩 
class ScrapQuiz(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'quiz')
