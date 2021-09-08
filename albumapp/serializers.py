from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import *


class AlbumUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name']


class AlbumImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImages
        fields = ['media']
        read_only_fields = ('album',)


class AlbumSerializer(serializers.ModelSerializer):
    album_images = AlbumImagesSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Album
        fields = ['id', 'user', 'name', 'album_images']

    # def to_representation(self, instance):
    #     rep = super(AlbumSerializer, self).to_representation(instance)
    #     rep['user'] = instance.user.username
    #     # rep['foreignkeyname'] = instance.foreignkeyname.actualfieldname in parent table
    #     return rep

    # def create(self, validated_data):
    #     print("I am in Create Method:>>>>>> : ")
    #     albumimages = validated_data.pop('album_images')
    #     album = Album.objects.create(**validated_data)
    #     for media in albumimages:
    #         file = AlbumImages.objects.create(album=album, **media)
    #         file.save()
    #     return album

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
