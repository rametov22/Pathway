# Generated by Django 5.1.5 on 2025-02-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests_app', '0002_teststart_test_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='teststart',
            name='title',
            field=models.CharField(default='', max_length=152),
            preserve_default=False,
        ),
    ]
