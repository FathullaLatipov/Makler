from rest_framework import serializers

from .models import StoreModel

# bu store niki
class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreModel
        fields = '__all__'

    def get_img_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image.url)
