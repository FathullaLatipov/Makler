from django.shortcuts import render
from rest_framework import generics

from products.models import CategoryModel, HouseModel, AmenitiesModel
from products.serializers import CategorySerializer, HomeSerializer, AmenitiesSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = CategoryModel.objects.order_by('pk')
    serializer_class = CategorySerializer


class AmenitiesListAPIView(generics.ListAPIView):
    queryset = AmenitiesModel.objects.order_by('pk')
    serializer_class = AmenitiesSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = HouseModel.objects.order_by('pk')
    serializer_class = HomeSerializer
