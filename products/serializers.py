from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.decorators import action

from products.helpers import modify_input_for_multiple_files
from products.models import CategoryModel, HouseModel, AmenitiesModel, MapModel, HouseImageModel, ImagesModel, \
    NewHouseImages


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
        fields = ['title', 'image', 'created_at']


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
                  'floor', 'floor_from', 'general', 'isBookmarked',
                  'images', 'uploaded_images',)
        extra_kwargs = {"user": {"read_only": True}}

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


# web
class WebHomeSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    # image = HomeImageSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'category', 'price', 'address',
                  'web_type', 'web_rental_type', 'web_object', 'web_building_type',
                  'isBookmarked', 'created_at', 'product_status'
                  ]


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
