# Generated by Django 3.2.6 on 2021-09-02 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0003_alter_albumimages_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimages',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albumimages', to='albumapp.album'),
        ),
    ]