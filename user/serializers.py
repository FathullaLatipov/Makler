from collections import defaultdict

from rest_framework import serializers

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
