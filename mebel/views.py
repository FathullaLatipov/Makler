from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView

from mebel.models import MebelCategoryModel, MebelModel
from mebel.serializers import MebelCategorySerializer, MebelSerializer


class MebelCategoryListAPIView(generics.ListAPIView):
    queryset = MebelCategoryModel.objects.order_by('pk')
    serializer_class = MebelCategorySerializer


class MebelListAPIView(generics.ListAPIView):
    queryset = MebelModel.objects.order_by('pk')
    serializer_class = MebelSerializer
