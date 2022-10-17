from rest_framework import serializers

from products.models import MapModel
from .models import MasterModel, MasterProfessionModel, MasterImagesModel


class MasterProfessionModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterProfessionModel
        fields = ['title']


class AddressModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MapModel
        exclude = ['id', 'created_at']


class ImageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterImagesModel
        exclude = ['id']


class MasterSerializer(serializers.ModelSerializer):
    profession = MasterProfessionModelSerializer(many=True)
    address = AddressModelSerializer()
    images = ImageModelSerializer(many=True)

    class Meta:
        model = MasterModel
        fields = ['name', 'address', 'avatar', 'profession', 'images', 'experience', 'isBookmarked']


class MasterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterModel
        fields = '__all__'

    def create(self, validated_data):
        return MasterModel.objects.create(**validated_data)


class MasterDetailSerializer(serializers.ModelSerializer):
    profession = MasterProfessionModelSerializer(many=True)
    address = AddressModelSerializer()
    images = ImageModelSerializer(many=True)

    class Meta:
        model = MasterModel
        exclude = ['password']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)
