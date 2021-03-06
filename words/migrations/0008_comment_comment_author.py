# Generated by Django 3.0.8 on 2020-09-09 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('words', '0007_remove_comment_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_author',
            field=models.ForeignKey(default=6, max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
            preserve_default=False,
        ),
    ]
