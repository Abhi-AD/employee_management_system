# Generated by Django 4.1.6 on 2023-08-18 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsletter',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.DeleteModel(
            name='JobCategory',
        ),
        migrations.DeleteModel(
            name='Joblocation',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
