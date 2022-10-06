from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MasterModel
from .serializers import MasterSerializer, MasterDetailSerializer


class MasterListAPIView(generics.ListAPIView):
    ''' Masters '''
    queryset = MasterModel.objects.order_by('pk')
    serializer_class = MasterSerializer


class MasterDetailAPIView(APIView):
    def get(self, request, pk):
        products = MasterModel.objects.get(id=pk)
        serializer = MasterDetailSerializer(products, context={'request': request})
        return Response(serializer.data)
