# Generated by Django 5.0.4 on 2024-04-29 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_uploadedfile_delete_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='uploaded_at',
        ),
    ]
