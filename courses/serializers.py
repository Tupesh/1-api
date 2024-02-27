from rest_framework import serializers
from . models import *

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model=course
        fields=('id','name','language','url','price')