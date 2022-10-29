from rest_framework import serializers

from .models import StoreModel


# bu store niki
class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = '__all__'
        read_only_fields = ['creator', ]

    def create(self, validated_data, creator):
        storemodel = StoreModel.objects.create(creator=creator,
                                               name=validated_data['name'],
                                               description=validated_data['description'],
                                               image=validated_data['image'],
                                               brand_image=validated_data['brand_image'],
                                               brand=validated_data['brand'],
                                               price=validated_data['price'],
                                               use_for=validated_data['use_for'],
                                               phoneNumber=validated_data['phoneNumber'],
                                               address=validated_data['address'],
                                               email=validated_data['email']
                                               )

        return storemodel

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)
