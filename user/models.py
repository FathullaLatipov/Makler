from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUser(AbstractUser):
    date_birth = models.DateField(null=True, blank=True)
    avatar_image = models.FileField(upload_to='custom_avatar_image', null=True, blank=True)
    phone_number = models.CharField(max_length=40, null=True, blank=True, unique=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
