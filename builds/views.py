from django.shortcuts import render
from rest_framework import generics
from .models import PcBuild
from .serializer import BuildSerializersDetailed, BuildSerializerCreate
# Create your views here.

class BuildList(generics.ListCreateAPIView):
    queryset = PcBuild.objects.all()
    serializer_class = BuildSerializersDetailed
    action_serializers = {
        'GET': BuildSerializersDetailed,
        'POST': BuildSerializerCreate
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.request.method in self.action_serializers:
                return self.action_serializers[self.request.method]
        return super(BuildList, self).get_serializer_class()
    
class BuildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PcBuild.objects.all()
    serializer_class = BuildSerializersDetailed 
    action_serializers = {
        'PUT': BuildSerializerCreate
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.request.method in self.action_serializers:
                return self.action_serializers[self.request.method]
        return super(BuildDetail, self).get_serializer_class()
