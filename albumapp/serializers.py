from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import *


class AlbumImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImages
        fields = ['id', 'media']
        read_only_fields = ('album',)


class AlbumSerializer(serializers.ModelSerializer):
    album_images = AlbumImagesSerializer(many=True)

    class Meta:
        model = Album
        fields = ['name', 'album_images']

    def create(self, **validated_data):
        print("it's in create Method:>>>>>> : ")
        albumimages = validated_data.pop('album_images')
        album = Album.objects.create(**validated_data)
        for image in albumimages:
            file = AlbumImages.objects.create(media=image, album=album)
            file.save()
        return album

    # def update(self, instance, validated_data):
    #     albumimages = validated_data.pop('album_images')
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     update_images = []
    #     existing_id = [e.id for e in instance.albumimages]
    #     for image in albumimages:
    #         pass
