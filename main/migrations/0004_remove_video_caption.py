# Generated by Django 5.0.4 on 2024-04-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='caption',
        ),
    ]
