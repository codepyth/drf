from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Album(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%H: %M: %S')}"


class AlbumImages(models.Model):
    album = models.ForeignKey(Album, related_name='album_images', on_delete=models.CASCADE)
    media = models.ImageField(upload_to='album/images')

    def __str__(self):
        return str(self.media)
