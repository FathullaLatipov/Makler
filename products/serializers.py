from rest_framework import serializers

from products.helpers import modify_input_for_multiple_files
from products.models import CategoryModel, HouseModel, AmenitiesModel, MapModel, HouseImageModel, ImagesModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title', 'image', 'created_at']


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenitiesModel
        fields = ['title', 'created_at']


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
class ImageSerializer(serializers.Serializer):
    image = serializers.FileField()

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_url(obj.image.url)


class HomeCreateSerializer(serializers.ModelSerializer):
    images = serializers.FileField()

    class Meta:
        model = ImagesModel
        fields = ['image', ]

    class Meta:
        model = HouseModel
        fields = ['title', 'descriptions', 'price',
                  'residential', 'number_of_rooms', 'floor', 'floor_from', 'general', 'isBookmarked',
                  'residential', 'amenities', 'images']
        extra_kwargs = {
            'images': {'required': False}
        }

    def to_representation(self, instance):
        context = super().to_representation(instance)
        # context['amenities'] = AmenitiesSerializer(instance.amenities, many=True).data
        # context['images'] = ImageSerializer(instance.images, many=True).data
        # context['category'] = CategorySerializer(instance.category).data
        # context['address'] = AddressSerializer(instance.address).data
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
