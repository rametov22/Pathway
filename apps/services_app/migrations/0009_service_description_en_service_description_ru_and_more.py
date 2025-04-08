# Generated by Django 5.1.5 on 2025-04-08 05:44

import mdeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0008_alter_consultationrequest_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description_en',
            field=mdeditor.fields.MDTextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_ru',
            field=mdeditor.fields.MDTextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_uz',
            field=mdeditor.fields.MDTextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='short_description_en',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='short_description_ru',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='short_description_uz',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_en',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_ru',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_uz',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
