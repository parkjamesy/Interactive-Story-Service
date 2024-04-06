from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StorySerializers
from .models import Story

# Create your views here.

class StoryView(viewsets.ModelViewSet):
    serializer_class = StorySerializers
    queryset = Story.objects.all()

