# Generated by Django 3.2.6 on 2021-09-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0007_alter_albumimages_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimages',
            name='media',
            field=models.CharField(max_length=30),
        ),
    ]
