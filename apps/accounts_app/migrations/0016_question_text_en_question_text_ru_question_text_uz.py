# Generated by Django 5.1.5 on 2025-04-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0015_alter_user_managers_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text_en',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text_ru',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='question',
            name='text_uz',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]
