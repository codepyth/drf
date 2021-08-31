from django.shortcuts import render
from rest_framework.response import Response
from .serializers import AlbumSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from albumapp import serializers
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.


# class AlbumView(generics.CreateAPIView):
#     queryset = Album
#     serializer_class = AlbumSerializer


# class AllAlbum(generics.RetrieveAPIView):
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer



@api_view(['POST'])
def addAlbum(request):
    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        files = request.FILES.getlist('file')

        print('files list...........', files)
        name = request.data['name']
        print('name: .......', name)
        
        if serializer.is_valid():
            name = Album.objects.create(name = request.data['name'])
            for f in files:
                file_instance = AlbumImages(file = f, album = name)
                file_instance.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def allAlbum(request):
#     if request.method == 'GET':
#         albumobj = Album.objects.all()
#         serializer = AlbumSerializer(albumobj, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def getAlbum(request, pk):
#     try:
#         albumobj = Album.objects.get(id=pk)
#         serializer = AlbumSerializer(albumobj)
#         return Response(serializer.data)
#     except:
#         return Response("No Records Found", status=status.HTTP_404_NOT_FOUND)


# @api_view(['PUT'])
# def updateAlbum(request, pk):
#     try:
#         albumobj = Album.objects.get(id=pk)
#         serializer = AlbumSerializer(albumobj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except:
#         return Response("No Records Found", status=status.HTTP_404_NOT_FOUND)


# @api_view(['DELETE'])
# def deleteAlbum(request, pk):
#     try:
#         albumobj = Album.objects.get(id=pk)
#         albumobj.delete()
#         return Response(request.data, status=status.HTTP_204_NO_CONTENT)
#     except:
#         return Response("No Records Found", status=status.HTTP_404_NOT_FOUND)
