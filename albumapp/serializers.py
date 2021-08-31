from rest_framework import serializers
from .models import *


class AlbumSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['name', 'album']


# class AlbumSerializer(serializers.ModelSerializer):
#     file = AlbumImageSerializer(many=True)
#     class Meta:
#         model = Album
#         fields = ['name', 'file']

    # def create(self, validated_data):
    #     image = validated_data.pop('file')
    #     name = validated_data.pop('name')
    #     for img in image:
    #         photo = Album.objects.create(
    #             name=name,
    #             file=img, **validated_data)
    #     return photo
