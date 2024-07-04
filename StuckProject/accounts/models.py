from django.db import models
from django.contrib.auth.models import User
from quiz.models import Folder, Quiz
from qna.models import QuestionRoom
from django.db.models.signals import post_delete
from django.dispatch import receiver

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30)
    univ = models.TextField(max_length=100)
    semester = models.IntegerField()
    resolution = models.CharField(max_length=50)
    introduce = models.CharField(max_length=100, blank=True)
    scrap_folders = models.ManyToManyField(Folder, through='ScrapFolder', related_name='folder_scrapped_by')
    scrap_quizs = models.ManyToManyField(Quiz, through="ScrapQuiz", related_name="quiz_scrapped_by")
    scrap_question_rooms = models.ManyToManyField(QuestionRoom, through="ScrapQuestionRoom", related_name="question_room_scrapped_by")
    recent_documents = models.ManyToManyField('RecentDocument', related_name='recent_documents_for_user', blank=True)


# 폴더 스크랩 
class ScrapFolder(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'folder')


# 퀴즈 스크랩 
class ScrapQuiz(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_folder_scrap")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'quiz')


# 질문 방 스크랩 QuestionRoom
class ScrapQuestionRoom(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,  related_name="user_questionroom_scrap")
    question_room = models.ForeignKey(QuestionRoom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question_room')


# 최근 열어본 문서
class RecentDocument(models.Model):
    content_type = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField() # 최근 열어본 문서가 Quiz 객체나 QuestionRoom 객체가 돌 수
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recent_documents_from_user')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.content_type} - {self.object_id}"
    

# Quiz, QuestionRoom 객체 삭제 시 RecentDocument도 삭제
@receiver(post_delete, sender=Quiz)
def delete_related_quiz_data(sender, instance, **kwargs):
    RecentDocument.objects.filter(content_type='quiz', object_id=instance.id).delete()

@receiver(post_delete, sender=QuestionRoom)
def delete_related_question_room_data(sender, instance, **kwargs):
    RecentDocument.objects.filter(content_type='questionroom', object_id=instance.id).delete()
