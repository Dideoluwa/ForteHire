# Generated by Django 4.0.5 on 2022-07-03 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quikapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_location',
        ),
    ]
