from rest_framework import serializers

from .models import MasterModel


class MasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterModel
        fields = '__all__'
