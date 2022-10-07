from django.shortcuts import render
from rest_framework import generics

from .models import StoreModel
from .serializers import StoreModelSerializer


class StoreModelAPIView(generics.ListAPIView):
    queryset = StoreModel.objects.order_by('pk')
    serializer_class = StoreModelSerializer
