from django.urls import path
from .views import addAlbum, GetAlbumById, GetAllAlbum

urlpatterns = [
    path('create/', addAlbum),
    path('allalbums/', GetAllAlbum),
    # path('album/<int:id>/', GetAlbumById),
    path('album/<str:slug>', GetAlbumById),
]
