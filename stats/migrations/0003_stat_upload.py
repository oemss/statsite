# Generated by Django 2.0.1 on 2018-01-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_remove_stat_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='upload',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]
