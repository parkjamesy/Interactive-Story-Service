from django.shortcuts import render
from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializers

# Create your views here.

class StoryView(viewsets.ModelViewSet):
    serializer_class = StorySerializers
    queryset = Story.objects.all()

