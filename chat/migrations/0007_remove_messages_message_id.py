# Generated by Django 3.0.3 on 2020-02-24 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20200224_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='message_id',
        ),
    ]
