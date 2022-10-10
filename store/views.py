from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics

from products.utils import get_wishlist_data
from .models import StoreModel
from rest_framework.response import Response
from .serializers import StoreModelSerializer


class StoreModelAPIView(generics.ListAPIView):
    queryset = StoreModel.objects.order_by('pk')
    serializer_class = StoreModelSerializer


def add_to_wishlist(request, pk):
    try:
        product = StoreModel.objects.get(pk=pk)
    except StoreModel.DoesNotExist:
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
