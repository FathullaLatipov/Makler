from rest_framework import serializers

from products.models import CategoryModel, HouseModel, AmenitiesModel, MasterModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title', 'image', 'created_at']


class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenitiesModel
        fields = ['title', 'created_at']


class HomeSerializer(serializers.ModelSerializer):
    amenities = AmenitiesSerializer(many=True)

    class Meta:
        model = HouseModel
        fields = '__all__'


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterModel
        fields = '__all__'
