import re
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from albumapp import serializers
# Create your views here.

@api_view(['POST'])
def addAlbum(request):
    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        albums = request.FILES.getlist('album')
        if albums:
            name = Album.objects.create(name=request.data['name'])
            # print(name)

            if serializer.is_valid():
                for file in albums:
                    album = AlbumImages.objects.create(media = file, album = name)
                serializer.save()
                return Response(serializer.data, status.HTTP_201_CREATED)
        return Response("Please upload the files", status.HTTP_400_BAD_REQUEST)
    return Response("Not found", status.HTTP_400_BAD_REQUEST)
