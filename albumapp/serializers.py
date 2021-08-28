from rest_framework import serializers
from .models import *


class AlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImages
        fields = ['album', 'file']

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
