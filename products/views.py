from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import CategoryModel, HouseModel, AmenitiesModel, MasterModel
from products.serializers import CategorySerializer, HomeSerializer, AmenitiesSerializer, MasterSerializer, \
    HomeDetailSerializer, HomeFavSerializer


class CategoryListAPIView(generics.ListAPIView):
    ''' Categories '''
    queryset = CategoryModel.objects.order_by('pk')
    serializer_class = CategorySerializer


class AmenitiesListAPIView(generics.ListAPIView):
    ''' Удобства (Amenities in product)'''
    queryset = AmenitiesModel.objects.order_by('pk')
    serializer_class = AmenitiesSerializer


class HouseListAPIView(generics.ListAPIView):
    ''' Products (Houses)'''
    queryset = HouseModel.objects.order_by('pk')
    serializer_class = HomeSerializer


class HouseFavListAPIView(generics.ListAPIView):
    ''' Fav (Houses)'''
    queryset = HouseModel.objects.order_by('pk')
    serializer_class = HomeFavSerializer


class HouseDetailAPIView(APIView):
    def get(self, request, pk):
        houses = HouseModel.objects.get(id=pk)
        serializer = HomeDetailSerializer(houses)
        return Response(serializer.data)


class MasterListAPIView(generics.ListAPIView):
    ''' Masters '''
    queryset = MasterModel.objects.order_by('pk')
    serializer_class = MasterSerializer
