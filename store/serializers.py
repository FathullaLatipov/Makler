from rest_framework import serializers

from .models import StoreModel


class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = '__all__'
