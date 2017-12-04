from time import timezone

import datetime
from rest_framework import serializers
from videos.models import Video


class VideoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    path = serializers.CharField(max_length=256)

    def create(self, validated_data):
        self.created_at = datetime.datetime.now()
        return Video.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.path = validated_data.get('path', instance.path)
        instance.created_at = datetime.datetime.now()
        instance.save()
        return instance
