from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User # 추후 User 모델과 연결

class Folder(MPTTModel):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="folders")
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    

class Quiz(models.Model):
    folder = models.ForeignKey(to=Folder, on_delete=models.CASCADE,related_name="quizs")
    file = models.FileField(upload_to="file/%Y/%m/%d/")
    created_at = models.DateField(auto_now_add=True)
    question_num = models.IntegerField()
    type = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    score = models.IntegerField(default=0)


class Question(models.Model):
    quiz = models.ForeignKey(to=Quiz, related_name="questions", on_delete = models.CASCADE)
    ai_question = models.CharField(max_length=100)
    user_answer = models.CharField(default='0', max_length=50)
    correct_answer = models.CharField(max_length=10)
    status = models.BooleanField(default=False)

    # user_answer와 correct_answer가 같다면 정답, 다르다면 오답
    def save(self, *args, **kwargs):
        if self.user_answer == self.correct_answer:
            self.status = True
        else:
            self.status = False
        super().save(*args, **kwargs)
