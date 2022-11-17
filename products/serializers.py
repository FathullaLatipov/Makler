from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.decorators import action

from products.helpers import modify_input_for_multiple_files
from products.models import CategoryModel, HouseModel, AmenitiesModel, MapModel, HouseImageModel, ImagesModel, \
    NewHouseImages, PriceListModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title', 'image', 'created_at']


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenitiesModel
        fields = ['title', 'image', 'created_at']


# web
class WebAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenitiesModel
        fields = ['id', 'title', 'image', 'created_at']


class WebPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceListModel
        fields = ['id', 'price_t']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapModel
        exclude = ['created_at']


class HomeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImageModel
        fields = ['property_id', 'image']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)


# class ImagesModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =
# class ImageSerializer(serializers.Serializer):
#     image = serializers.FileField(use_url=True)
#
#
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewHouseImages
        fields = ['images']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_url(obj.image.url)


class APPHomeCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    # address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['title', 'descriptions', 'price', 'app_currency', 'app_type', 'typeOfRent', 'typeOfHouse',
                  'typeOfObject', 'app_ipoteka', 'app_mebel', 'type', 'address', 'general', 'residential',
                  'number_of_rooms', 'floor', 'floor_from', 'building_type', 'amenities', 'product_status',
                  'images', 'uploaded_images',]
        # extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        title = validated_data.get('title')
        descriptions = validated_data.get('descriptions')
        price = validated_data.get('price')
        app_currency = validated_data.get('app_currency')
        app_type = validated_data.get('app_type')
        typeOfRent = validated_data.get('typeOfRent')
        typeOfHouse = validated_data.get('typeOfHouse')
        typeOfObject = validated_data.get('typeOfObject')
        app_ipoteka = validated_data.get('app_ipoteka')
        app_mebel = validated_data.get('app_mebel')
        type = validated_data.get('type')
        address = validated_data.get('address')
        general = validated_data.get('general')
        residential = validated_data.get('residential')
        number_of_rooms = validated_data.get('number_of_rooms')
        floor = validated_data.get('floor')
        floor_from = validated_data.get('floor_from')
        building_type = validated_data.get('building_type')
        product_status = validated_data.get('product_status')
        amenities = validated_data.get('amenities')
        titles = [i.title for i in amenities]
        amenities_titles = AmenitiesModel.objects.filter(title__in=titles)
        new_product = HouseModel.objects.create(
            title=title,
            descriptions=descriptions,
            price=price,
            app_currency=app_currency,
            app_type=app_type,
            typeOfRent=typeOfRent,
            typeOfHouse=typeOfHouse,
            typeOfObject=typeOfObject,
            app_ipoteka=app_ipoteka,
            app_mebel=app_mebel,
            type=type,
            address=address,
            general=general,
            residential=residential,
            number_of_rooms=number_of_rooms,
            floor=floor,
            floor_from=floor_from,
            building_type=building_type,
            product_status=product_status,
        )
        new_product.amenities.add(*amenities_titles)
        for uploaded_item in uploaded_data:
            new_product_image = NewHouseImages.objects.create(product=new_product, images=uploaded_item)
        return new_product

    def get_img_url(self, obj):
        urls = []
        for i in obj.images.all():
            myurl = self.context['request'].build_absolute_uri(i.image.url)
            urls.append(myurl)
        return urls

class NewHomeCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    # address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ('title', 'descriptions', 'price', 'residential', 'number_of_rooms',
                  'floor', 'floor_from', 'general', 'web_type', 'web_rental_type', 'web_object', 'web_building_type',
                  'isBookmarked',
                  'images', 'uploaded_images',)
        # extra_kwargs = {"user": {"read_only": True}}

    @swagger_auto_schema(operation_description='Upload file...', )
    @action(detail=False, methods=['post'])
    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_product = HouseModel.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            new_product_image = NewHouseImages.objects.create(product=new_product, images=uploaded_item)
        return new_product

    def get_img_url(self, obj):
        urls = []
        for i in obj.images.all():
            myurl = self.context['request'].build_absolute_uri(i.image.url)
            urls.append(myurl)
        return urls

    # def save(self, **kwargs):
    #     kwargs["creator"] = self.fields["creator"].get_default()
    #     return super().save(**kwargs)

    # def to_representation(self, instance):
    #     context = super().to_representation(instance)
    #     context['images'] = ImageSerializer(instance.images, many=True).data
    #     return context


class HomeCreateSerializer(serializers.ModelSerializer):
    images = serializers.FileField()

    class Meta:
        model = ImagesModel
        fields = ['image', ]

    class Meta:
        model = HouseModel
        fields = ['title', 'descriptions', 'price', 'address',
                  'residential', 'number_of_rooms', 'floor', 'floor_from', 'general', 'isBookmarked',
                  'images']
        extra_kwargs = {
            'images': {'required': False}
        }

    def to_representation(self, instance):
        context = super().to_representation(instance)
        # context['amenities'] = AmenitiesSerializer(instance.amenities, many=True).data
        # context['images'] = ImageSerializer(instance.images, many=True).data
        # context['category'] = CategorySerializer(instance.category).data
        context['address'] = AddressSerializer(instance.address).data
        return context

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_url(obj.image.url)
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get("title", instance.title)
    #     instance.descriptions = validated_data.get("descriptions", instance.descriptions)
    #     instance.price = validated_data.get("price", instance.price)
    #     instance.general = validated_data.get("general", instance.general)
    #     instance.residential = validated_data.get("residential", instance.residential)
    #     instance.number_of_rooms = validated_data.get("number_of_rooms", instance.number_of_rooms)
    #     instance.floor = validated_data.get("floor", instance.floor)
    #     instance.floor_from = validated_data.get("floor_from", instance.floor_from)
    #     # instance.image = validated_data.get("image", instance.image)
    #     instance.save()
    #     return instance


#  bu homeniki
class HomeSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    # image = HomeImageSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'category', 'price', 'address', 'isBookmarked', 'created_at', 'product_status']


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceListModel
        fields = ['price_t']


# web
class NewAllWebHomeCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    amenities = WebAmenitiesSerializer(many=True)
    price_type = PriceListSerializer()

    # address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'price', 'price_type', 'amenities',
                  'web_type', 'web_rental_type', 'web_address_title', 'web_address_latitude', 'web_address_longtitude', 'web_rental_type', 'web_object', 'web_building_type',
                  'isBookmarked', 'created_at', 'product_status', 'images', 'uploaded_images', 'creator'
                  ]


class NewWebHomeCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    # address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'creator', 'title', 'price', 'price_type', 'amenities',
                  'web_type', 'web_address_title', 'web_address_latitude', 'web_address_longtitude', 'web_rental_type',
                  'web_object', 'web_building_type',
                  'isBookmarked', 'created_at', 'product_status', 'images', 'uploaded_images'
                  ]
        extra_kwargs = {"creator": {"read_only": True}}

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        price_types = validated_data.pop('price_type')
        amenities = validated_data.get('amenities')
        title = validated_data.get('title')
        web_address_title = validated_data.get('web_address_title')
        web_address_latitude = validated_data.get('web_address_latitude')
        web_address_longtitude = validated_data.get('web_address_longtitude')
        web_type = validated_data.get('web_type')
        web_rental_type = validated_data.get('web_rental_type')
        web_object = validated_data.get('web_object')
        web_building_type = validated_data.get('web_building_type')
        price = validated_data.get('price')
        creator = self.context['request'].user
        titles = [i.title for i in amenities]
        amenities_titles = AmenitiesModel.objects.filter(title__in=titles)
        price_t = PriceListModel.objects.get(price_t=price_types)
        target_objs = HouseModel.objects.create(price_type=price_t, title=title, price=price,
                                                web_address_title=web_address_title,
                                                web_address_latitude=web_address_latitude,
                                                web_address_longtitude=web_address_longtitude,
                                                web_type=web_type, web_rental_type=web_rental_type,
                                                web_object=web_object, web_building_type=web_building_type,
                                                creator=creator
                                                )
        target_objs.amenities.add(*amenities_titles)
        for uploaded_item in uploaded_data:
            new_product_image = NewHouseImages.objects.create(product=target_objs, images=uploaded_item)
        return target_objs


    def get_img_url(self, obj):
        urls = []
        for i in obj.images.all():
            myurl = self.context['request'].build_absolute_uri(i.image.url)
            urls.append(myurl)
        return urls


class HomeArchiveSerializer(serializers.ModelSerializer):
    product_status = serializers.PrimaryKeyRelatedField(
        queryset=HouseModel.objects.filter(product_status='ARCHIVED')
    )

    class Meta:
        model = HouseModel
        fields = '__all__'


class HomeFavSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'price', 'address', 'isBookmarked', 'created_at']


class HomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title']


class HomeDetailSerializer(serializers.ModelSerializer):
    category = HomeCategorySerializer()
    address = AddressSerializer()
    # image = HomeImageSerializer(many=True)
    amenities = AmenitiesSerializer(many=True)

    # choices = serializers.SerializerMethodField('get_choices')

    class Meta:
        model = HouseModel
        fields = '__all__'
