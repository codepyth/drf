# Generated by Django 3.2.6 on 2021-08-31 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0004_rename_file_albumimages_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimages',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_name', to='albumapp.album'),
        ),
    ]