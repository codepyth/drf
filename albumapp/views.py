from django.views import generic
from rest_framework import generics, serializers
from rest_framework.response import Response
from .serializers import AlbumImagesSerializer, AlbumSerializer
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

# class AddAlbum(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#
#     def post(self, request, *args, **kwargs):
#         serializer = AlbumSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         obj = Album.objects.all()
#         serializer = AlbumSerializer(obj, many=True)
#         return Response(serializer.data)


@api_view(['POST'])
def AddAlbum(request):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


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
def GetAlbumById(request, id):
    obj = Album.objects.get(id=id)
    serializer = AlbumSerializer(obj, many=True)
    return Response(serializer.data)
