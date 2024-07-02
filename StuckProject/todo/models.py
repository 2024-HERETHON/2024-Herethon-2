from django.db import models
from accounts.models import CustomUser

class Routine(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_routins")
    name = models.CharField(max_length=100, default='루틴')

    def __str__(self):
        return self.name

class ToDo(models.Model):
    date = models.DateField(auto_now_add=True)
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='할 일')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

