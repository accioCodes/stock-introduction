# Generated by Django 3.1 on 2020-08-21 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backprojectapi', '0003_auto_20200821_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jointochat',
            name='postId',
        ),
    ]