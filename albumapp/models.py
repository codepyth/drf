from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    file = models.ImageField(upload_to='album/images')

    def __str__(self):
        return self.name