# Generated by Django 5.1.5 on 2025-02-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts_app', '0005_successstories_short_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='successstories',
            name='university',
        ),
        migrations.AddField(
            model_name='successstories',
            name='short_name_university',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
