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
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = ['image',]

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_url(obj.image.url)


class NewHomeCreateSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=True)

    class Meta:
        model = HouseModel
        fields = ('title', 'descriptions', 'price', 'address', 'image', 'residential', 'number_of_rooms', 'floor', 'floor_from', 'general', 'isBookmarked',
                  'images',)
        extra_kwargs = {
            'images': {'required': False, "read_only": True}
        }
    # manaqa qsechi? hozi
    def create(self, validated_data, creator, imagelist):
        housemodel = HouseModel.objects.create(creator=creator,
                                               title=validated_data['title'],
                                               descriptions=validated_data['descriptions'],
                                               price=validated_data['price'],
                                               address=validated_data['address'],
                                               residential=validated_data['residential'],
                                               number_of_rooms=validated_data['number_of_rooms'],
                                               floor=validated_data['floor'],
                                               floor_from=validated_data['floor_from'],
                                               general=validated_data['general'],
                                               )
        for img_name in imagelist:
            img = ImagesModel.objects.create(image=img_name)
            housemodel.images.add(img)
        housemodel.save()
        return housemodel

    def get_img_url(self, obj):
        urls = []
        for i in obj.images.all():
            myurl = self.context['request'].build_absolute_uri(i.image.url)
            urls.append(myurl)
        return urls

    def to_representation(self, instance):
        context = super().to_representation(instance)
        print('+++++++++++++++++++++++', instance.images.all())
        context['images'] = ImageSerializer(instance.images.all(), many=True).data
        return context


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
