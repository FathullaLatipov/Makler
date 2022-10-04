from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MasterModel
from .serializers import MasterSerializer


class MasterListAPIView(generics.ListAPIView):
    ''' Masters '''
    queryset = MasterModel.objects.order_by('pk')
    serializer_class = MasterSerializer
