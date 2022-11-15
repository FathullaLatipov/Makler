from rest_framework import serializers

from user.models import CustomUser
from .models import StoreModel, StoreAmenities


# bu store niki
class StoreAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreAmenities
        fields = ['title',]


class StoreModelSerializer(serializers.ModelSerializer):
    # store_amenitites = StoreAmenitiesSerializer(many=True)
    uploaded_image = serializers.FileField(
        max_length=10000,
        allow_empty_file=False,
        write_only=True
    )

    class Meta:
        model = StoreModel
        fields = ['id', 'name', 'description', 'brand', 'price', 'use_for',
                  'phoneNumber', 'address', 'email', 'uploaded_image', 'creator']
        # read_only_fields = ['creator', ]

    def create(self, validated_data):
        print(self.data)
        print(validated_data)
        image_data = validated_data.pop('uploaded_image')
        store_obj = StoreModel(**validated_data)
        store_obj.image = image_data
        store_obj.save()
        return store_obj
        # storemodel = StoreModel.objects.create(creator=creator,
        #                                        name=validated_data['name'],
        #                                        description=validated_data['description'],
        #                                        image=validated_data['image'],
        #                                        brand_image=validated_data['brand_image'],
        #                                        brand=validated_data['brand'],
        #                                        price=validated_data['price'],
        #                                        use_for=validated_data['use_for'],
        #                                        phoneNumber=validated_data['phoneNumber'],
        #                                        address=validated_data['address'],
        #                                        email=validated_data['email']
        #                                        )



    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)
