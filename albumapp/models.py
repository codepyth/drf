from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    def __str__(self):
        return self.name

class AlbumImages(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='album/images')