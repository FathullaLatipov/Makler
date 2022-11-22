from rest_framework import serializers

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
        fields = ['name', 'address', 'avatar', 'profession', 'images', 'experience', 'isBookmarked', 'owner']


# create master POST
class MasterCreateSerializer(serializers.ModelSerializer):
    # profession = MasterProfessionModelSerializer(many=True)
    # address = AddressModelSerializer()

    class Meta:
        model = MasterModel
        fields = ['name', 'email', 'image', 'phone', 'address', 'avatar', 'profession',
                  'descriptions', 'experience', 'owner',
                  ]
        extra_kwargs = {"owner": {"read_only": True}}

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
