from django.views import generic
from rest_framework import generics, serializers
from rest_framework.response import Response
from .serializers import AlbumImagesSerializer, AlbumSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


# Create your views here.

@api_view(['POST'])
def AddAlbum(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetAllAlbum(request):
    obj = Album.objects.all()
    serializer = AlbumSerializer(obj, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def GetAlbumById(request, id):
    obj = Album.objects.get(id=id)
    serializer = AlbumSerializer(obj, many=True)
    return Response(serializer.data)
