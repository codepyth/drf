from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    albumimages = StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['name', 'albumimages']
