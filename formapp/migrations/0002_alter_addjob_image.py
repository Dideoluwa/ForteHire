# Generated by Django 4.0.5 on 2022-07-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addjob',
            name='image',
            field=models.ImageField(blank=True, upload_to='jobimages'),
        ),
    ]
