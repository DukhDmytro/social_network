# Generated by Django 3.0.3 on 2020-02-24 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20200224_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.CharField(max_length=100),
        ),
    ]
