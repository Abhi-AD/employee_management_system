# Generated by Django 4.1.6 on 2023-08-29 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetail',
            name='feature_image',
            field=models.ImageField(default=datetime.datetime(2023, 8, 29, 15, 55, 33, 789690, tzinfo=datetime.timezone.utc), upload_to='EMP_images/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
