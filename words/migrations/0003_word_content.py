# Generated by Django 3.0.8 on 2020-08-26 22:35

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_remove_word_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='content',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]