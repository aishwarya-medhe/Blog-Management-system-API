# Generated by Django 4.2.11 on 2024-03-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author_profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
