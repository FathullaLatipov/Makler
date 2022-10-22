from django.http import JsonResponse
from rest_framework import generics, mixins, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from masters.models import MasterModel
from store.models import StoreModel
from .models import ImagesModel, MapModel
from rest_framework.decorators import parser_classes

from products.helpers import modify_input_for_multiple_files
from products.models import CategoryModel, HouseModel, AmenitiesModel, HouseImageModel
from products.serializers import CategorySerializer, HomeSerializer, AmenitiesSerializer, \
    HomeDetailSerializer, HomeFavSerializer, HomeCreateSerializer, HomeImageSerializer
from products.utils import get_wishlist_data


class CategoryListAPIView(generics.ListAPIView):
    ''' Categories '''
    queryset = CategoryModel.objects.order_by('pk')
    serializer_class = CategorySerializer


class AmenitiesListAPIView(generics.ListAPIView):
    ''' Удобства (Amenities in product)'''
    queryset = AmenitiesModel.objects.order_by('pk')
    serializer_class = AmenitiesSerializer


class HouseImageAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_images = HouseImageModel.objects.all()
        serializer = HomeImageSerializer(all_images, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        property_id = request.data['property_id']

        images = dict((request.data).lists())['image']
        flag = 1
        arr = []
        for img_name in images:
            modified_data = modify_input_for_multiple_files(property_id, img_name)
            file_serializer = HomeImageSerializer(data=modified_data)
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)


class HouseListAPIView(generics.ListAPIView):
    ''' Products (Houses)'''
    queryset = HouseModel.objects.filter(draft=False)
    serializer_class = HomeSerializer


def add_to_wishlist(request, pk):
    try:
        product = HouseModel.objects.get(pk=pk)
    except HouseModel.DoesNotExist:
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


class HouseFavListAPIView(generics.ListAPIView):
    ''' Fav (Houses)'''
    queryset = HouseModel.objects.order_by('pk')
    serializer_class = HomeFavSerializer


class HouseDetailAPIView(APIView):
    def get(self, request, pk):
        houses = HouseModel.objects.get(id=pk)
        serializer = HomeDetailSerializer(houses, context={'request': request})
        return Response(serializer.data)


# @parser_classes([MultiPartParser, FormParser])
class HouseAddCreateAPIView(APIView):
    serializer_class = HomeCreateSerializer

    def get_object(self, pk=None):
        if pk:
            pass
        house = HouseModel.objects.all()
        return house

    def get(self, request, **kwargs):
        if 'pk' in kwargs:
            pass
        house = self.get_object()
        serializer = self.serializer_class(house, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # serializer = self.serializer_class(data=request.data)
        print(request.FILES.getlist('images'))
        category = CategoryModel.objects.get(id=int(request.data['category']))
        address = MapModel.objects.get(id=int(request.data['address']))
        house = HouseModel.objects.create(
            title=request.data['title'],
            category=category,
            descriptions=request.data['descriptions'],
            price=request.data['price'],
            type=request.data['type'],
            rental_type=request.data['rental_type'],
            object=request.data['object'],
            address=address,
            general=request.data['general'],
            residential=request.data['residential'],
        )
        image = request.FILES.getlist('images')
        for img_name in image:
            img = ImagesModel.objects.create(image=img_name)
            house.images.add(img)
        for i in request.data['amenities']:
            house.amenities.add(int(i))
            house.save()

        return Response(self.serializer_class(house).data, status=status.HTTP_201_CREATED)


# class HouseAddCreateAPIView(mixins.CreateModelMixin, GenericViewSet):
#     queryset = HouseModel.objects.all()
#     serializer_class = HomeCreateSerializer
#     super(GenericViewSet, self).()
#     image = dict((validated_data).lists())['images']
#     print('++++++++++++++++++++++++', image)
#     for img_name in image:
#         modified_data = modify_input_for_multiple_files(img_name)
#
#     def crate(self, request):
#         pas

#
#         form_serializers = HomeCreateSerializer(data=request.data)
#         if form_serializers.is_valid(raise_exception=True):
#             # print('hello2')
#             # form_serializers.save()
#             # print('hello3')
#             # arr.append(form_serializers.data)
#             # print('hello4')
#             form_serializers.save()
#             form_serializers.instance.images = modified_data
#         else:
#             flag = 0
#             print('hello5')
#
#     if flag == 1:
#         return Response(arr, status=status.HTTP_201_CREATED)
#     else:
#         return Response(arr, status=status.HTTP_400_BAD_REQUEST)

#
# def get_serializer_context(self):
#     return {'request': self.request}


class HouseUpdateAPIView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = HouseModel.objects.all()
    serializer_class = HomeCreateSerializer

    def update(self, request, *args, **kwargs):
        user_profile = self.get_object()
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class HouseDestroyAPIView(mixins.DestroyModelMixin, GenericViewSet):
    queryset = HouseModel.objects.all()
    serializer_class = HomeCreateSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#user app bormi alohida daa

        