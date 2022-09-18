from rest_framework import serializers

from products.models import CategoryModel, HouseModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['title', 'image', 'created_at']


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseModel
        fields = '__all__'
