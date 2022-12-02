from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from products.models import MapModel
from user.models import CustomUser
from .models import MasterModel, MasterProfessionModel, MasterImagesModel


# master profiessions
class MasterProfessionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProfessionModel
        fields = ['title']


# master address
class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapModel
        exclude = ['id', 'created_at']


# master images
class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterImagesModel
        fields = ['images']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_url(obj.image.url)


# all masters
class MasterSerializer(serializers.ModelSerializer):
    profession = MasterProfessionModelSerializer(many=True)
    address = AddressModelSerializer()

    class Meta:
        model = MasterModel
        fields = ['pk', 'name', 'address', 'avatar', 'profession', 'images', 'experience', 'isBookmarked', 'owner']


# create master POST
class MasterCreateSerializer(serializers.ModelSerializer):
    # profession = MasterProfessionModelSerializer(many=True)
    password = serializers.CharField(write_only=True, required=False,)
    # address = AddressModelSerializer()

    class Meta:
        model = MasterModel
        fields = ['name', 'email', 'phone', 'address_title', 'address_latitude', 'address_longitude',
                  'password', 'profession',
                  'descriptions', 'experience', 'owner',
                  ]
        extra_kwargs = {"owner": {"read_only": True}}

    def create(self, validated_data):
        mastermodel = MasterModel.objects.create(
                                                 name=validated_data['name'],
                                                 password=validated_data['password'],
                                                 email=validated_data['email'],
                                                 phone=validated_data['phone'],
                                                 address_title=validated_data['address_title'],
                                                 address_latitude=validated_data['address_latitude'],
                                                 address_longitude=validated_data['address_longitude'],
                                                 descriptions=validated_data['descriptions'],
                                                 experience=validated_data['experience']
                                                 )
        for i in validated_data['profession']:
            mastermodel.profession.add(i.id)
            mastermodel.save()
        return mastermodel

    def get_img_url(self, obj):
        urls = []
        for i in obj.images.all():
            myurl = self.context['request'].build_absolute_uri(i.image.url)
            urls.append(myurl)
        return urls

    def to_representation(self, instance):
        context = super().to_representation(instance)
        # context['profession'] = MasterProfessionModelSerializer(instance.profession, many=True).data
        # context['images'] = ImageModelSerializer(instance.images, many=True).data
        return context


class MasterDetailSerializer(serializers.ModelSerializer):
    profession = MasterProfessionModelSerializer(many=True)
    address = AddressModelSerializer()
    images = ImageModelSerializer(many=True)

    class Meta:
        model = MasterModel
        exclude = ['password']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'posts']
