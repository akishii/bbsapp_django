from django.db import models
from django.utils import timezone

# Create your models here.
class BoardModel(models.Model):

    #BoardModelテーブルに各フィールドを作成
    title = models.CharField(max_length=50)
    content = models.TextField()
    regist_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=20)
    good = models.IntegerField(null=True, blank=True, default=0)
