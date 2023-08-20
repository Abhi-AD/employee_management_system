# Generated by Django 4.1.6 on 2023-08-20 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web_app', '0002_delete_newsletter_remove_post_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=100)),
                ('feature_image', models.ImageField(upload_to='Job_post_images/%Y/%m/%d')),
                ('status', models.CharField(choices=[('active', 'Active'), ('in_active', 'Inactive')], default='active', max_length=20)),
                ('description', models.TextField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('views_count', models.PositiveBigIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.jobcategory')),
                ('location', models.ManyToManyField(to='web_app.joblocation')),
            ],
        ),
    ]
