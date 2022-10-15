from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from products.utils import get_wishlist_data
from .models import MasterModel
from .serializers import MasterSerializer, MasterDetailSerializer, MasterCreateSerializer


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


class MasterAddCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
    queryset = MasterModel.objects.all()
    serializer_class = MasterCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class MasterUpdateAPIView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = MasterModel.objects.all()
    serializer_class = MasterCreateSerializer

    def update(self, request, *args, **kwargs):
        user_profile = self.get_object()
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MasterDestroyAPIView(mixins.DestroyModelMixin, GenericViewSet):
    queryset = MasterModel.objects.all()
    serializer_class = MasterCreateSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
