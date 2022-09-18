from django.shortcuts import render
from rest_framework import generics

from products.models import CategoryModel, HouseModel
from products.serializers import CategorySerializer, HomeSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = CategoryModel.objects.order_by('pk')
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = HouseModel.objects.order_by('pk')
    serializer_class = HomeSerializer
