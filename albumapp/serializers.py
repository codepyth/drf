from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import *

class AlbumImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AlbumImages
        fields = ['id', 'media']
        read_only_fields = ('album', )

class AlbumSerializer(serializers.ModelSerializer):
    album_images = AlbumImagesSerializer(many=True)
    
    class Meta:
        model = Album
        fields = ['id', 'name', 'album_images']

    def create(self, validated_data):
        print("Working............", validated_data)
        albumimages = validated_data.pop('album_images')
        album = Album.objects.create(**validated_data)
        for image in albumimages:
            file = AlbumImages.objects.create(media=image, album=album)
            file.save()
        return album
