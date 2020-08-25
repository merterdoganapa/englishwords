from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Word(models.Model):
    word_en = models.CharField(max_length=50)
    word_tr = models.CharField(max_length=50)
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    category = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.word_en