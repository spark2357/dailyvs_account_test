# Generated by Django 4.2.5 on 2023-09-19 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='custom_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='voted_polls',
        ),
    ]