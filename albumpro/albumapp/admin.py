from django.contrib import admin
from .models import Album, AlbumImages
# Register your models here.

admin.site.register([Album, AlbumImages])