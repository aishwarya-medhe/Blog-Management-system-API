# Generated by Django 4.2.11 on 2024-03-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0009_alter_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
