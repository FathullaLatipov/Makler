from django.http import JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from products.utils import get_wishlist_data
from .models import StoreModel
from rest_framework.response import Response
from .serializers import StoreModelSerializer


class StoreModelAPIView(generics.ListAPIView):
    queryset = StoreModel.objects.order_by('pk')
    serializer_class = StoreModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['use_for', 'how_store_service']


class RandomStoreModelAPIView(generics.ListAPIView):
    queryset = StoreModel.objects.order_by('?')
    serializer_class = StoreModelSerializer


class SearchStoreModelAPIView(generics.ListAPIView):
    queryset = StoreModel.objects.order_by('pk')
    serializer_class = StoreModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['address']


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


class StoreDetailAPIView(APIView):
    def get(self, request, pk):
        houses = StoreModel.objects.get(id=pk)
        serializer = StoreModelSerializer(houses, context={'request': request})
        return Response(serializer.data)


# class StoreAddCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
#     queryset = StoreModel.objects.all()
#     serializer_class = StoreModelSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}

class StoreAddCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = StoreModelSerializer
    parser_classes = [MultiPartParser]
    queryset = StoreModel.objects.all()
    permission_classes = [IsAuthenticated, ]

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.create(validated_data=serializer.validated_data, creator=request.user)
    #     return Response(serializer.data)
    # def get_object(self):
    #     return StoreModel.objects.all()
    #
    # def get(self, request):
    #     serailizer = self.serializer_class(self.get_object(), context={'request': request}, many=True)
    #     return Response(serailizer.data, status=200)

    # def post(self, request):


class StoreUpdateAPIView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = StoreModel.objects.all()
    serializer_class = StoreModelSerializer

    def update(self, request, *args, **kwargs):
        user_profile = self.get_object()
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class StoreDestroyAPIView(mixins.DestroyModelMixin, GenericViewSet):
    queryset = StoreModel.objects.all()
    serializer_class = StoreModelSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
