# Generated by Django 4.2.11 on 2024-03-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0007_remove_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
