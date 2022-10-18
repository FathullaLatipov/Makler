from rest_framework import serializers

from products.models import CategoryModel, HouseModel, AmenitiesModel, MapModel, HouseImageModel


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
        fields = '__all__'

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)


class HomeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseModel
        fields = ['title', 'category', 'descriptions', 'price', 'image', 'type', 'rental_type', 'object', 'address', 'general',
                  'residential', 'amenities']

    def create(self, validated_data):
        housemodel = HouseModel.objects.create(title=validated_data['title'],
                                               descriptions=validated_data['descriptions'],
                                               category=validated_data['category'],
                                               price=validated_data['price'], type=validated_data['type'],
                                               rental_type=validated_data['rental_type'],
                                               object=validated_data['object'], address=validated_data['address'],
                                               general=validated_data['general'],
                                               residential=validated_data['residential']
                                               )

        for i in validated_data['amenities']:
            housemodel.amenities.add(i.id)
        for j in validated_data['image']:
            housemodel.image.add(j.id)
        housemodel.save()
        return housemodel

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['amenities'] = AmenitiesSerializer(instance.amenities, many=True).data
        context['image'] = HomeImageSerializer(instance.image, many=True).data
        context['category'] = CategorySerializer(instance.category).data
        context['address'] = AddressSerializer(instance.address).data
        return context
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


class HomeSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    image = HomeImageSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'category', 'price', 'address', 'image', 'isBookmarked', 'created_at']


class HomeFavSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'price', 'address', 'image', 'isBookmarked', 'created_at']


class HomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title']


class HomeDetailSerializer(serializers.ModelSerializer):
    category = HomeCategorySerializer()
    address = AddressSerializer()
    image = HomeImageSerializer(many=True)
    amenities = AmenitiesSerializer(many=True)

    # choices = serializers.SerializerMethodField('get_choices')

    class Meta:
        model = HouseModel
        fields = '__all__'
