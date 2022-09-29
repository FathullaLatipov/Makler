from django.shortcuts import render
from rest_framework import generics

from products.models import CategoryModel, HouseModel, AmenitiesModel, MasterModel
from products.serializers import CategorySerializer, HomeSerializer, AmenitiesSerializer, MasterSerializer


class CategoryListAPIView(generics.ListAPIView):
    ''' Categories '''
    queryset = CategoryModel.objects.order_by('pk')
    serializer_class = CategorySerializer


class AmenitiesListAPIView(generics.ListAPIView):
    ''' Удобства (Amenities in product)'''
    queryset = AmenitiesModel.objects.order_by('pk')
    serializer_class = AmenitiesSerializer


class ProductListAPIView(generics.ListAPIView):
    ''' Products (Houses)'''
    queryset = HouseModel.objects.order_by('pk')
    serializer_class = HomeSerializer


class MasterListAPIView(generics.ListAPIView):
    ''' Masters '''
    queryset = MasterModel.objects.order_by('pk')
    serializer_class = MasterSerializer
