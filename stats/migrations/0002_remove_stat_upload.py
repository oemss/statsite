# Generated by Django 2.0.1 on 2018-01-14 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='upload',
        ),
    ]
