from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User # 추후 User 모델과 연결

class Folder(MPTTModel):
    user = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name