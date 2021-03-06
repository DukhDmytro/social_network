# Generated by Django 3.0.3 on 2020-02-24 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20200224_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='title',
        ),
        migrations.AddField(
            model_name='messages',
            name='message_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
