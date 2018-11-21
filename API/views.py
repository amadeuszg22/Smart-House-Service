#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from .serializers import UserSerializer, GroupSerializer
from configpanel.models import configweather,configdev
#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from .serializers import configweatherSerializer, configdevSerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


from rest_framework import generics

class ChannelList(generics.ListCreateAPIView):
    queryset = configweather.objects.all()
    serializer_class = configweatherSerializer


class ChannelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = configweather.objects.all()
    serializer_class = configweatherSerializer

class DevList(generics.ListCreateAPIView):
    queryset = configdev.objects.all()
    serializer_class = configdevSerializer

class DevDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = configdev.objects.all()
    serializer_class = configdevSerializer
