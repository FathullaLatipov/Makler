from django.http import JsonResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication

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
    @swagger_auto_schema(
        operation_summary="Получения Мастера(ID)",
        operation_description="Метод получения данных мастера. Помимо типа данных и токен авторизации, передаётся только ID мастера.",
    )
    def get(self, request, pk):
        products = MasterModel.objects.get(id=pk)
        serializer = MasterDetailSerializer(products, context={'request': request})
        return Response(serializer.data)


#
# class MasterAddCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
#     queryset = MasterModel.objects.all()
#     serializer_class = MasterCreateSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}


class MasterCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
    queryset = MasterModel.objects.all()
    serializer_class = MasterCreateSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = MasterModel.objects.all()
        serializer = MasterCreateSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MasterCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def get_object(self):
#     return MasterModel.objects.all()
#
# def get(self, request):
#     serailizer = self.serializer_class(self.get_object(), context={'request': request}, many=True)
#     return Response(serailizer.data, status=200)
#
# def post(self, request):
#     serializer = self.serializer_class(data=request.data)
#     if serializer.is_valid():
#         serializer.create(validated_data=serializer.validated_data, owner=request.user)
#     return Response(serializer.data)


class MasterUpdateAPIView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = MasterModel.objects.all()
    serializer_class = MasterCreateSerializer

    @swagger_auto_schema(
        operation_summary="Обновления мастера(ID)",
        operation_description="Метод обновления данных мастера. Помимо типа данных и токен авторизации, передаётся только ID мастера.",
    )
    def update(self, request, *args, **kwargs):
        user_profile = self.get_object()
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class MasterDestroyAPIView(mixins.DestroyModelMixin, GenericViewSet):
    queryset = MasterModel.objects.all()
    serializer_class = MasterCreateSerializer

    @swagger_auto_schema(
        operation_summary="Удаления мастера(ID)",
        operation_description="Метод для удаления данных мастера. Помимо типа данных и токен авторизации, передаётся только ID мастера.",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
