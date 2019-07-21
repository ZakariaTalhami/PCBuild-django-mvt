from rest_framework import serializers
from .models import Cpu, Memory, Mobo, Storage, Videocard

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = [
            'id',
            'manufacturer',
            'series',
            'model_name',
            'part_number',
            'family',
            'cores',
            'threads',
            'base_clock',
            'boost_clock',
        ]

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = [
            'id',
            'model_name',
            'manufacturer',
            'part_number',
            'speed',
            'frequency',
            'memory_type',
            'isdual',
            'memory',
            'cas_latency',
            'isecc',
            'price',
        ]

class MoboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobo
        fields = [
            'id',
            'manufactuer',
            'part_number',
            'socket',
            'chipset',
            'form_factor',
            'ram_slots',
            'max_ram',
            'sata',
            'm2',
            'pcie',
            'price',
        ]

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = [
            'id',
            'name',
            'part_number',
            'capacity',
            'cache',
            'interface',
            'price',
        ]

class VideocardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videocard
        fields = [
            'id',
            'manufacturer',
            'part_number',
            'model_name',
            'chipset',
            'memory',
            'base_clock',
            'boost_clock',
            'price',
        ]