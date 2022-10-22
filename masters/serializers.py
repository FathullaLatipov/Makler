from rest_framework import serializers

from products.models import MapModel
from user.models import CustomUser
from .models import MasterModel, MasterProfessionModel, MasterImagesModel


class MasterProfessionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterProfessionModel
        fields = ['title']


# qaren bita narsa korsataman ok mi? ok boldi

class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapModel
        exclude = ['id', 'created_at']


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterImagesModel
        exclude = ['id']


# bu masterniki all masters
class MasterSerializer(serializers.ModelSerializer):
    profession = MasterProfessionModelSerializer(many=True)
    address = AddressModelSerializer()
    images = ImageModelSerializer(many=True)

    class Meta:
        model = MasterModel
        fields = ['name', 'address', 'avatar', 'profession', 'images', 'experience', 'isBookmarked']


# create master POST
class MasterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterModel
        fields = ['image', 'name', 'email', 'phone', 'address', 'avatar', 'profession', 'images', 'descriptions', 'experience']

    def create(self, validated_data):
        mastermodel = MasterModel.objects.create(
                                                 image=validated_data['image'],
                                                 name=validated_data['name'],
                                                 email=validated_data['email'],
                                                 phone=validated_data['phone'],
                                                 address=validated_data['address'],
                                                 avatar=validated_data['avatar'],
                                                 descriptions=validated_data['descriptions'],
                                                 experience=validated_data['experience']
                                                 )
        for i in validated_data['profession']:
            mastermodel.profession.add(i.id)
        for j in validated_data['images']:
            mastermodel.images.add(j.id)
        mastermodel.save()
        return mastermodel

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['profession'] = MasterProfessionModelSerializer(instance.profession, many=True).data
        context['images'] = ImageModelSerializer(instance.images, many=True).data
        return context


# class MasterCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MasterModel
#         fields = ['creator', 'image', 'name', 'email', 'phone', 'address', 'avatar', 'profession', 'images',
#                   'descriptions',
#                   'experience']
#         read_only_fields = ['creator', ]
#
#         # ko§relichi ok
#
#     def create(self, validated_data, user):
#         mastermodel = MasterModel.objects.create(creator=user,
#                                                  image=validated_data['image'],
#                                                  name=validated_data['name'],
#                                                  email=validated_data['email'],
#                                                  phone=validated_data['phone'],
#                                                  address=validated_data['address'],
#                                                  avatar=validated_data['avatar'],
#                                                  descriptions=validated_data['descriptions'],
#                                                  experience=validated_data['experience']
#                                                  )
#
#         for i in validated_data['profession']:
#             mastermodel.profession.add(i.id)
#         for j in validated_data['images']:
#             mastermodel.images.add(j.id)
#         mastermodel.save()
#         return mastermodel
#
#     def to_representation(self, instance):
#         context = super().to_representation(instance)
#         context['profession'] = MasterProfessionModelSerializer(instance.profession, many=True).data
#         context['images'] = ImageModelSerializer(instance.images, many=True).data
#         return context

class MasterDetailSerializer(serializers.ModelSerializer):
    profession = MasterProfessionModelSerializer(many=True)
    address = AddressModelSerializer()
    images = ImageModelSerializer(many=True)

    class Meta:
        model = MasterModel
        exclude = ['password']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)


# asdasdasd
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MasterModel
        fields = ['id', 'name', 'phone', 'owner']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'posts']
