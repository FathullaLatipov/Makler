from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from products.utils import get_wishlist_data
from .models import MasterModel
from .serializers import MasterSerializer, MasterDetailSerializer


class MasterListAPIView(generics.ListAPIView):
    ''' Masters '''
    queryset = MasterModel.objects.order_by('pk')
    serializer_class = MasterSerializer


def add_to_wishlist(request, pk):
    try:
        product = MasterModel.objects.get(pk=pk)
    except MasterModel.DoesNotExist:
        return Response(data={'status': False})
    wishlist = request.session.get('wishlist', [])
    if product.pk in wishlist:
        wishlist.remove(product.pk)
        data = {'status': True, 'added': False}
    else:
        wishlist.append(product.pk)
        data = {'status': True, 'added': True}
    request.session['wishlist'] = wishlist

    data['wishlist_len'] = get_wishlist_data(wishlist)
    return JsonResponse(data)


class MasterDetailAPIView(APIView):
    def get(self, request, pk):
        products = MasterModel.objects.get(id=pk)
        serializer = MasterDetailSerializer(products, context={'request': request})
        return Response(serializer.data)
