# Generated by Django 3.2.6 on 2021-08-31 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0003_alter_albumimages_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albumimages',
            old_name='file',
            new_name='media',
        ),
    ]