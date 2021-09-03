from re import I
from django.urls import path
from .views import AddAlbum, GetAlbumById, GetAllAlbum

urlpatterns = [
    path('create/', AddAlbum),
    path('albums/', GetAllAlbum),
    path('album/delete/<int:id>/', GetAlbumById),
]