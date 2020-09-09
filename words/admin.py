from django.contrib import admin
from .models import Word,Comment
# Register your models here.


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['word_en','word_tr','category','author','created_date']




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['word','comment_content']