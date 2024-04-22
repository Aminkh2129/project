# Generated by Django 4.2 on 2024-04-20 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0007_remove_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='todo', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
