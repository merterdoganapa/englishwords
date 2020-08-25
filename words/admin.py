from django.contrib import admin
from .models import Word
# Register your models here.


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['word_en','word_tr','category','author','created_date']