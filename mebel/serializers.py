from rest_framework import serializers

from mebel.models import MebelCategoryModel, MebelModel, NewMebelImages


class MebelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MebelCategoryModel
        fields = '__all__'


class MebelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewMebelImages
        fields = ['images']

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_url(obj.image.url)


class MebelSerializer(serializers.ModelSerializer):
    images = MebelImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = MebelModel
        fields = '__all__'
