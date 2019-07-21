from django.shortcuts import render
from rest_framework import generics
# models
from .models import Cpu, Memory, Mobo, Storage, Videocard
from .serializers import CpuSerializer, MemorySerializer, MoboSerializer, StorageSerializer, VideocardSerializer

class CpuList(generics.ListCreateAPIView):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class CpuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class MemoryList(generics.ListCreateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer

class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer

class MoboList(generics.ListCreateAPIView):
    queryset = Mobo.objects.all()
    serializer_class = MoboSerializer

class MoboDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobo.objects.all()
    serializer_class = MoboSerializer

class StorageList(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

class StorageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

class VideocardList(generics.ListCreateAPIView):
    queryset = Videocard.objects.all()
    serializer_class = VideocardSerializer

class VideocardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Videocard.objects.all()
    serializer_class = VideocardSerializer