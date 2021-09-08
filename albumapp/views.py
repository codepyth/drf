from django.views import generic
from rest_framework import generics, serializers
from rest_framework.response import Response
from .serializers import AlbumImagesSerializer, AlbumSerializer, AlbumUpdateSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# from rest_framework import generics
import json


# Create your views here.


# @api_view(['POST'])
# def AddAlbum(request):
#     serializer = AlbumSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def addAlbum(request):
    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        albums = request.FILES.getlist('album_images')
        if albums:
            name = Album.objects.create(name=request.data['name'])
            if serializer.is_valid():
                for file in albums:
                    AlbumImages.objects.create(media=file, album=name)
                # serializer.save()
                return Response("Album created Successfully", status.HTTP_201_CREATED)
        return Response("Files Not Found", status.HTTP_400_BAD_REQUEST)
    return Response("Not found", status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'PUT'])
def UpdateAlbumName(request, id):
    if request.method == 'PUT':
        obj = Album.objects.get(id=id)
        print("hereeeeee....................")
        serializer = AlbumUpdateSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors)
    return Response({"Message: ": "This method is not allowed"}, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetAllAlbum(request):
    if request.method == 'GET':
        obj = Album.objects.all()
        serializer = AlbumSerializer(obj, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    else:
        res = {
            "Message": "Sorry, method not allowed"
        }
        return Response(res, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetAlbumByUserId(request, slug):
    obj = Album.objects.filter(user=slug)
    serializer = AlbumSerializer(obj, many=True)
    return Response(serializer.data)

#
# class GetAlbumById(generics.ListAPIView):
#     serializer_class = AlbumSerializer
#
#     def get_queryset(request):
#         # name = self.kwargs['slug']
#         name = request.query_params.get('name')
#         return Album.objects.filter(name=name)
