from collections import defaultdict

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.models import CustomUser


class CheckTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, required=False,
                                      write_only=True)

    password2 = serializers.CharField(max_length=255, required=False,
                                      write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        extra_kwargs = dict(
            password=dict(required=True)
        )

    def validate(self, attrs):
        errors = defaultdict(list)
        emails = CustomUser.objects.filter(email=attrs['email'])
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if emails.exists():
            errors['email'].append('Email has already')
        if errors:
            raise serializers.ValidationError(errors)
        if password1 != password2:
            raise serializers.ValidationError(
                {'status': "Password do not match"}
            )
        return attrs

    def create(self, validated_data):
        password1 = validated_data.pop('password1', None)
        password2 = validated_data.pop('password2', None)
        user = super().create(validated_data)
        if password1:
            user.set_password(password1)
            user.set_password(password2)
            user.save()
        return user

    def update(self, instance, validated_data):
        password1 = validated_data.pop('password1', None)
        password2 = validated_data.pop('password2', None)
        user = super().update(instance, validated_data)
        if password1:
            user.set_password(password1)
            user.set_password(password2)
            user.save()
        return user


class UserDataSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False,
                                     validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = '__all__'

    def validate(self, attrs):
        if password := attrs.get('password'):
            attrs['password'] = make_password(password)
        return attrs


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user_data'] = UserDataSerializer(self.user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
