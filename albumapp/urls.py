from django.urls import path
from .views import addAlbum, GetAllAlbum, GetAlbumByUserId, UpdateAlbumName

urlpatterns = [
    path('create/', addAlbum),
    path('create/<int:id>/', UpdateAlbumName),
    path('allalbums/', GetAllAlbum),
    # path('album/<int:id>/', GetAlbumById),
    path('album/<str:slug>/', GetAlbumByUserId),
]
