from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication

from products.utils import get_wishlist_data
from .models import MasterModel
from .serializers import MasterSerializer, MasterDetailSerializer, MasterCreateSerializer, PostSerializer


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

#
# class MasterAddCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
#     queryset = MasterModel.objects.all()
#     serializer_class = MasterCreateSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}


class MasterCreateAPIView(APIView):
    serializer_class = MasterCreateSerializer

    def get_object(self):
        return MasterModel.objects.all()

    def get(self, request):
        serailizer = self.serializer_class(self.get_object(), context={'request': request}, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(validated_data=serializer.validated_data, owner=request.user)
        return Response(serializer.data)




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





class PostList(generics.ListCreateAPIView):
    queryset = MasterModel.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    # def perform_create(self, serializer):
    #     print(serializer)
    #     print('+++==+++++', self.request.user.is_authenticated)
    #     serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MasterModel.objects.all()
    serializer_class = PostSerializer
