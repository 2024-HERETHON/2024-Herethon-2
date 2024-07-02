from django.db import models
from django.utils import timezone

class Routine(models.Model):
    name = models.CharField(max_length=100, default='루틴')

    def __str__(self):
        return self.name

class ToDo(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, default='할 일')
    completed = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now().date())

    def __str__(self):
        return self.description

