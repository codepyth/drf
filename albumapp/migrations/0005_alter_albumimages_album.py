# Generated by Django 3.2.6 on 2021-09-02 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0004_alter_albumimages_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimages',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albumapp.album'),
        ),
    ]
