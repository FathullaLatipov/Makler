from rest_framework import serializers

from products.models import CategoryModel, HouseModel, AmenitiesModel, MasterModel, MasterActivity


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


class MasterActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterActivity
        fields = ['title']


class MasterSerializer(serializers.ModelSerializer):
    activity = MasterActivitySerializer(many=True)

    class Meta:
        model = MasterModel
        fields = '__all__'
