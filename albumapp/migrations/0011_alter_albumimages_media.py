# Generated by Django 3.2.6 on 2021-09-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0010_alter_albumimages_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimages',
            name='media',
            field=models.ImageField(upload_to='album/images'),
        ),
    ]
