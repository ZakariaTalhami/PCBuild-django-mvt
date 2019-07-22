from rest_framework import serializers
from .models import PcBuild
from parts.serializers import CpuSerializer, MoboSerializer, VideocardSerializer, StorageSerializer, MemorySerializer

class BuildSerializersDetailed(serializers.ModelSerializer):
    cpu = CpuSerializer()
    mobo = MoboSerializer()
    storage = StorageSerializer(many=True)
    videocard = VideocardSerializer(many=True)
    memory = MemorySerializer(many=True)

    class Meta:
        model =  PcBuild
        fields = [
            'id',
            'name',
            'description',
            'cpu',
            'mobo',
            'storage',
            'videocard',
            'memory',
        ]

class BuildSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model =  PcBuild
        fields = [
            'id',
            'name',
            'description',
            'cpu',
            'mobo',
            'storage',
            'videocard',
            'memory',
        ]