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
        exclude = ['image']


class HomeSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    image = HomeImageSerializer(many=True)

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'price', 'address', 'image', 'isBookmarked', 'created_at']


class HomeFavSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = HouseModel
        fields = ['id', 'title', 'price', 'address', 'image', 'isBookmarked', 'created_at']


class HomeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseModel
        fields = '__all__'
