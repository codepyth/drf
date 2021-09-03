from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    def __str__(self):
        return self.name


class AlbumImages(models.Model):
    album = models.ForeignKey(Album, related_name='album_images', on_delete=models.CASCADE)
    media = models.ImageField(upload_to='album/images')

    def __str__(self):
        return str(self.album.name)