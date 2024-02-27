from django.shortcuts import render
from rest_framework import viewsets
from . models import *
from . serializers import *


# Create your views here.

class courseView(viewsets.ModelViewSet):
    queryset=course.objects.all()
    serializer_class=courseSerializer