from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from mebel.models import MebelCategoryModel, MebelModel
from mebel.serializers import MebelCategorySerializer, MebelSerializer, AllMebelSerializer, UpdateAllMebelSerializer


class MebelCategoryListAPIView(generics.ListAPIView):
    queryset = MebelCategoryModel.objects.order_by('pk')
    serializer_class = MebelCategorySerializer


class MebelListAPIView(generics.ListAPIView):
    queryset = MebelModel.objects.order_by('pk')
    serializer_class = AllMebelSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['web_address_title']


class RandomMebelListAPIView(generics.ListAPIView):
    queryset = MebelModel.objects.order_by('?')
    serializer_class = AllMebelSerializer


class MebelCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
    queryset = MebelModel.objects.all()
    serializer_class = MebelSerializer
    permission_classes = [IsAuthenticated, ]


class MebelUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MebelModel.objects.all()
    serializer_class = UpdateAllMebelSerializer


class MebelDetailAPIView(APIView):
    def get(self, request, pk):
        products = MebelModel.objects.get(id=pk)
        serializer = AllMebelSerializer(products, context={'request': request})
        return Response(serializer.data)


class MebelDestroyAPIView(mixins.DestroyModelMixin, GenericViewSet):
    queryset = MebelModel.objects.all()
    serializer_class = MebelSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
