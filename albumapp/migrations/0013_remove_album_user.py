# Generated by Django 3.2.6 on 2021-09-07 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0012_album_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
    ]