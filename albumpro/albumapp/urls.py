from re import I
from django.urls import path
from .views import addAlbum
# , allAlbum, deleteAlbum, getAlbum, updateAlbum

urlpatterns = [
    path('create/', addAlbum),
    # path('all/', allAlbum),
    # path('detail/<int:pk>/', getAlbum),
    # path('update/<int:pk>/', updateAlbum),
    # path('delete/<int:pk>/', deleteAlbum),
]