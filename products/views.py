from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import CategoryModel, HouseModel, AmenitiesModel
from products.serializers import CategorySerializer, HomeSerializer, AmenitiesSerializer, \
    HomeDetailSerializer, HomeFavSerializer, HomeCreateSerializer


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


class HouseAddCreateAPIView(APIView):
    def post(self, request):
        serializers = HomeCreateSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({'post': serializers.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = HouseModel.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = HomeCreateSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
