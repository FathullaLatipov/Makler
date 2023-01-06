from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from mebel.models import MebelCategoryModel, MebelModel
from mebel.serializers import MebelCategorySerializer, MebelSerializer, AllMebelSerializer


class MebelCategoryListAPIView(generics.ListAPIView):
    queryset = MebelCategoryModel.objects.order_by('pk')
    serializer_class = MebelCategorySerializer


class MebelListAPIView(generics.ListAPIView):
    queryset = MebelModel.objects.order_by('pk')
    serializer_class = AllMebelSerializer


class MebelCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
    queryset = MebelModel.objects.all()
    serializer_class = MebelSerializer
    permission_classes = [IsAuthenticated, ]


class MebelUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MebelModel.objects.all()
    serializer_class = MebelSerializer


class MebelDestroyAPIView(mixins.DestroyModelMixin, GenericViewSet):
    queryset = MebelModel.objects.all()
    serializer_class = MebelSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)