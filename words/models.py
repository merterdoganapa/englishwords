from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Word(models.Model):
    word_en = models.CharField(max_length=50)
    word_tr = models.CharField(max_length=50)
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    category = models.CharField(max_length=20)
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.word_en


class Comment(models.Model):
    word = models.ForeignKey(Word,on_delete = models.CASCADE,verbose_name = "Word",related_name="comments")
    comment_author = models.ForeignKey(User,on_delete=models.CASCADE,max_length = 50,verbose_name = "Author")
    comment_content = models.CharField(max_length = 200,verbose_name = "Sample Sentence")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']