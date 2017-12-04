# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from videos import models
from videos import serializers


def index(request):
    videos = [video.to_dict() for video in models.Video.objects.all()]
    return HttpResponse(videos)


class ListVideosView(APIView):
    def get(self, request):
        videos = [video.to_dict() for video in models.Video.objects.all()]
        return Response(videos)

    def post(self, request):
        serializer = serializers.VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        videos = [video.to_dict() for video in models.Video.objects.all()]
        return Response(videos)